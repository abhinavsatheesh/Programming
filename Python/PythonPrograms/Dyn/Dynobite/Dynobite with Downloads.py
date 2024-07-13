from tkPDFViewer import tkPDFViewer as pdf
from tkinter import *
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *
from PySide2 import QtCore
from functools import partial
import json
import validators
import sys
import os

_web_actions = [QWebEnginePage.Back, QWebEnginePage.Forward,
                QWebEnginePage.Reload,
                QWebEnginePage.Undo, QWebEnginePage.Redo,
                QWebEnginePage.Cut, QWebEnginePage.Copy,
                QWebEnginePage.Paste, QWebEnginePage.SelectAll]


class WebEngineView(QWebEngineView):

    enabled_changed = QtCore.Signal(QWebEnginePage.WebAction, bool)

    @staticmethod
    def web_actions():
        return _web_actions

    @staticmethod
    def minimum_zoom_factor():
        return 5

    @staticmethod
    def maximum_zoom_factor():
        return 5

    def __init__(self, tab_factory_func, window_factory_func):
        super(WebEngineView, self).__init__()
        self._tab_factory_func = tab_factory_func
        self._window_factory_func = window_factory_func
        page = self.page()
        self._actions = {}
        for web_action in WebEngineView.web_actions():
            action = page.action(web_action)
            action.changed.connect(self._enabled_changed)
            self._actions[action] = web_action

    def is_web_action_enabled(self, web_action):
        return self.page().action(web_action).isEnabled()

    def createWindow(self, window_type):
        if (window_type == QWebEnginePage.WebBrowserTab or
            window_type == QWebEnginePage.WebBrowserBackgroundTab):
            return self._tab_factory_func()
        return self._window_factory_func()

    def _enabled_changed(self):
        action = self.sender()
        web_action = self._actions[action]
        self.enabled_changed.emit(web_action, action.isEnabled())


class HistoryModel(QAbstractTableModel):

    def __init__(self, history, parent=None):
        super(HistoryModel, self).__init__(parent)
        self._history = history

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Web Page' if section == 0 else 'URL'
        return None

    def rowCount(self, index=QModelIndex()):
        return self._history.count()

    def columnCount(self, index=QModelIndex()):
        return 2

    def item_at(self, model_index):
        return self._history.itemAt(model_index.row())

    def data(self, index, role=Qt.DisplayRole):
        item = self.item_at(index)
        column = index.column()
        if role == Qt.DisplayRole:
            return item.title() if column == 0 else item.url().toString()
        return None

    def refresh(self):
        self.beginResetModel()
        self.endResetModel()


class HistoryWindow(QTreeView):

    open_url = Signal(QUrl)

    def __init__(self, history, parent):
        super(HistoryWindow, self).__init__(parent)

        self._model = HistoryModel(history, self)
        self.setModel(self._model)
        self.activated.connect(self._activated)

        screen = QApplication.desktop().screenGeometry(parent)
        self.resize(screen.width() / 3, screen.height() / 3)
        self._adjustSize()

    def refresh(self):
        self._model.refresh()
        self._adjustSize()

    def _adjustSize(self):
        if (self._model.rowCount() > 0):
            self.resizeColumnToContents(0)

    def _activated(self, index):
        item = self._model.item_at(index)
        self.open_url.emit(item.url())


# A Find tool bar (bottom area)
class FindToolBar(QToolBar):

    find = QtCore.Signal(str, QWebEnginePage.FindFlags)

    def __init__(self):
        super(FindToolBar, self).__init__()
        self._line_edit = QLineEdit()
        self._line_edit.setClearButtonEnabled(True)
        self._line_edit.setPlaceholderText("Find...")
        self._line_edit.setMaximumWidth(300)
        self._line_edit.returnPressed.connect(self._find_next)
        self.addWidget(self._line_edit)

        self._previous_button = QToolButton()
        style_icons = ':/qt-project.org/styles/commonstyle/images/'
        self._previous_button.setIcon(QIcon(style_icons + 'up-32.png'))
        self._previous_button.clicked.connect(self._find_previous)
        self.addWidget(self._previous_button)

        self._next_button = QToolButton()
        self._next_button.setIcon(QIcon(style_icons + 'down-32.png'))
        self._next_button.clicked.connect(self._find_next)
        self.addWidget(self._next_button)

        self._case_sensitive_checkbox = QCheckBox('Case Sensitive')
        self.addWidget(self._case_sensitive_checkbox)

        self._hideButton = QToolButton()
        self._hideButton.setShortcut(QKeySequence(Qt.Key_Escape))
        self._hideButton.setIcon(QIcon(style_icons + 'closedock-16.png'))
        self._hideButton.clicked.connect(self.hide)
        self.addWidget(self._hideButton)

    def focus_find(self):
        self._line_edit.setFocus()

    def _emit_find(self, backward):
        needle = self._line_edit.text().strip()
        if needle:
            flags = QWebEnginePage.FindFlags()
            if self._case_sensitive_checkbox.isChecked():
                flags |= QWebEnginePage.FindCaseSensitively
            if backward:
                flags |= QWebEnginePage.FindBackward
            self.find.emit(needle, flags)

    def _find_next(self):
        self._emit_find(False)

    def _find_previous(self):
        self._emit_find(True)


class DownloadWidget(QProgressBar):
    """Lets you track progress of a QWebEngineDownloadItem."""
    finished = QtCore.Signal()
    remove_requested = QtCore.Signal()

    def __init__(self, download_item):
        super(DownloadWidget, self).__init__()
        self._download_item = download_item
        download_item.finished.connect(self._finished)
        download_item.downloadProgress.connect(self._download_progress)
        download_item.stateChanged.connect(self._update_tool_tip())
        path = download_item.path()
        self.setMaximumWidth(300)
        # Shorten 'PySide2-5.11.0a1-5.11.0-cp36-cp36m-linux_x86_64.whl'...
        description = QFileInfo(path).fileName()
        description_length = len(description)
        if description_length > 30:
            description = '{}...{}'.format(description[0:10],
                                           description[description_length - 10:])
        self.setFormat('{} %p%'.format(description))
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setValue(0)
        self.setMaximum(100)
        self._update_tool_tip()
        # Force progress bar text to be shown on macoS by using 'fusion' style
        if sys.platform == 'darwin':
            self.setStyle(QStyleFactory.create('fusion'))

    @staticmethod
    def open_file(file):
        QDesktopServices.openUrl(QUrl.fromLocalFile(file))

    @staticmethod
    def open_download_directory():
        path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        DownloadWidget.open_file(path)

    def state(self):
        return self._download_item.state()

    def _update_tool_tip(self):
        path = self._download_item.path()
        tool_tip = "{}\n{}".format(self._download_item.url().toString(),
                                   QDir.toNativeSeparators(path))
        total_bytes = self._download_item.totalBytes()
        if total_bytes > 0:
            tool_tip += "\n{}K".format(total_bytes / 1024)
        state = self.state()
        if state == QWebEngineDownloadItem.DownloadRequested:
            tool_tip += "\n(requested)"
        elif state == QWebEngineDownloadItem.DownloadInProgress:
            tool_tip += "\n(downloading)"
        elif state == QWebEngineDownloadItem.DownloadCompleted:
            tool_tip += "\n(completed)"
        elif state == QWebEngineDownloadItem.DownloadCancelled:
            tool_tip += "\n(cancelled)"
        else:
            tool_tip += "\n(interrupted)"
        self.setToolTip(tool_tip)

    def _download_progress(self, bytes_received, bytes_total):
        self.setValue(int(100 * bytes_received / bytes_total))

    def _finished(self):
        self._update_tool_tip()
        self.finished.emit()

    def _launch(self):
        DownloadWidget.open_file(self._download_item.path())

    def mouseDoubleClickEvent(self, event):
        if self.state() == QWebEngineDownloadItem.DownloadCompleted:
            self._launch()

    def contextMenuEvent(self, event):
        state = self.state()
        context_menu = QMenu()
        launch_action = context_menu.addAction("Launch")
        launch_action.setEnabled(state == QWebEngineDownloadItem.DownloadCompleted)
        show_in_folder_action = context_menu.addAction("Show in Folder")
        show_in_folder_action.setEnabled(state == QWebEngineDownloadItem.DownloadCompleted)
        cancel_action = context_menu.addAction("Cancel")
        cancel_action.setEnabled(state == QWebEngineDownloadItem.DownloadInProgress)
        remove_action = context_menu.addAction("Remove")
        remove_action.setEnabled(state != QWebEngineDownloadItem.DownloadInProgress)

        chosen_action = context_menu.exec_(event.globalPos())
        if chosen_action == launch_action:
            self._launch()
        elif chosen_action == show_in_folder_action:
            path = QFileInfo(self._download_item.path()).absolutePath()
            DownloadWidget.open_file(path)
        elif chosen_action == cancel_action:
            self._download_item.cancel()
        elif chosen_action == remove_action:
            self.remove_requested.emit()


class BrowserTabWidget(QTabWidget):
    """Enables having several tabs with QWebEngineView."""

    url_changed = QtCore.Signal(QUrl)
    enabled_changed = QtCore.Signal(QWebEnginePage.WebAction, bool)
    download_requested = QtCore.Signal(QWebEngineDownloadItem)

    def __init__(self, window_factory_function):
        super(BrowserTabWidget, self).__init__()
        self.setTabsClosable(True)
        self._window_factory_function = window_factory_function
        self._webengineviews = []
        self._history_windows = {}  # map WebengineView to HistoryWindow
        self.currentChanged.connect(self._current_changed)
        self.tabCloseRequested.connect(self.handle_tab_close_request)
        self._actions_enabled = {}
        for web_action in WebEngineView.web_actions():
            self._actions_enabled[web_action] = False

        tab_bar = self.tabBar()
        tab_bar.setSelectionBehaviorOnRemove(QTabBar.SelectPreviousTab)
        tab_bar.setContextMenuPolicy(Qt.CustomContextMenu)
        tab_bar.customContextMenuRequested.connect(self._handle_tab_context_menu)

    def add_browser_tab(self):
        qurl = QUrl("https://www.google.com")
        factory_func = partial(BrowserTabWidget.add_browser_tab, self)
        web_engine_view = WebEngineView(factory_func,
                                        self._window_factory_function)
        index = self.count()
        web_engine_view.setUrl(qurl)
        self._webengineviews.append(web_engine_view)
        title = 'Tab {}'.format(index + 1)
        self.addTab(web_engine_view, title)
        page = web_engine_view.page()
        page.titleChanged.connect(self._title_changed)
        page.iconChanged.connect(self._icon_changed)
        page.profile().downloadRequested.connect(self._download_requested)
        web_engine_view.urlChanged.connect(self._url_changed)
        web_engine_view.enabled_changed.connect(self._enabled_changed)
        self.setCurrentIndex(index)
        return web_engine_view

    def _on_fullscreen_requested(self, request):
        request.accept()
        on = request.toggleOn()

    def load(self, url):
        index = self.currentIndex()
        if index >= 0 and url.isValid():
            self._webengineviews[index].setUrl(url)

    def find(self, needle, flags):
        index = self.currentIndex()
        if index >= 0:
            self._webengineviews[index].page().findText(needle, flags)

    def url(self):
        index = self.currentIndex()
        return self._webengineviews[index].url() if index >= 0 else QUrl()

    def _url_changed(self, url):
        index = self.currentIndex()
        if index >= 0 and self._webengineviews[index] == self.sender():
                self.url_changed.emit(url)

    def _title_changed(self, title):
        index = self._index_of_page(self.sender())
        if (index >= 0):
            self.setTabText(index, BookmarkWidget.short_title(title))

    def _icon_changed(self, icon):
        index = self._index_of_page(self.sender())
        if (index >= 0):
            self.setTabIcon(index, icon)

    def _enabled_changed(self, web_action, enabled):
        index = self.currentIndex()
        if index >= 0 and self._webengineviews[index] == self.sender():
            self._check_emit_enabled_changed(web_action, enabled)

    def _check_emit_enabled_changed(self, web_action, enabled):
        if enabled != self._actions_enabled[web_action]:
            self._actions_enabled[web_action] = enabled
            self.enabled_changed.emit(web_action, enabled)

    def _current_changed(self, index):
        self._update_actions(index)
        self.url_changed.emit(self.url())

    def _update_actions(self, index):
        if index >= 0 and index < len(self._webengineviews):
            view = self._webengineviews[index]
            for web_action in WebEngineView.web_actions():
                enabled = view.is_web_action_enabled(web_action)
                self._check_emit_enabled_changed(web_action, enabled)

    def back(self):
        self._trigger_action(QWebEnginePage.Back)

    def forward(self):
        self._trigger_action(QWebEnginePage.Forward)

    def reload(self):
        self._trigger_action(QWebEnginePage.Reload)

    def undo(self):
        self._trigger_action(QWebEnginePage.Undo)

    def redo(self):
        self._trigger_action(QWebEnginePage.Redo)

    def cut(self):
        self._trigger_action(QWebEnginePage.Cut)

    def copy(self):
        self._trigger_action(QWebEnginePage.Copy)

    def paste(self):
        self._trigger_action(QWebEnginePage.Paste)

    def select_all(self):
        self._trigger_action(QWebEnginePage.SelectAll)

    def show_history(self):
        index = self.currentIndex()
        if index >= 0:
            webengineview = self._webengineviews[index]
            history_window = self._history_windows.get(webengineview)
            if not history_window:
                history = webengineview.page().history()
                history_window = HistoryWindow(history, self)
                history_window.open_url.connect(self.load)
                history_window.setWindowFlags(history_window.windowFlags()
                                              | Qt.Window)
                history_window.setWindowTitle('History')
                self._history_windows[webengineview] = history_window
            else:
                history_window.refresh()
            history_window.show()
            history_window.raise_()

    def zoom_factor(self):
        return self._webengineviews[0].zoomFactor() if self._webengineviews else 1.0

    def set_zoom_factor(self, z):
        for w in self._webengineviews:
            w.setZoomFactor(z)

    def _handle_tab_context_menu(self, point):
        index = self.tabBar().tabAt(point)
        if index < 0:
            return
        tab_count = len(self._webengineviews)
        context_menu = QMenu()
        new_tab_action = context_menu.addAction("New Tab")
        refresh_action = context_menu.addAction("Reload")
        duplicate_tab_action = context_menu.addAction("Duplicate Tab")
        close_other_tabs_action = context_menu.addAction("Close Other Tabs")
        close_other_tabs_action.setEnabled(tab_count > 1)
        close_tabs_to_the_right_action = context_menu.addAction("Close Tabs to the Right")
        close_tabs_to_the_right_action.setEnabled(index < tab_count - 1)
        close_tab_action = context_menu.addAction("&Close Tab")
        chosen_action = context_menu.exec_(self.tabBar().mapToGlobal(point))
        if chosen_action == duplicate_tab_action:
            current_url = self.url()
            self.add_browser_tab().load(current_url)
        elif chosen_action == new_tab_action:
            current_url = "https://www.google.com"
            self.add_browser_tab().load(current_url)
        elif chosen_action == refresh_action:
            self.reload()            
        elif chosen_action == close_other_tabs_action:
            for t in range(tab_count - 1, -1, -1):
                if t != index:
                    self.handle_tab_close_request(t)
        elif chosen_action == close_tabs_to_the_right_action:
            for t in range(tab_count - 1, index, -1):
                self.handle_tab_close_request(t)
        elif chosen_action == close_tab_action:
            self.handle_tab_close_request(index)

    def handle_tab_close_request(self, index):
        if (index >= 0 and self.count() > 1):
            webengineview = self._webengineviews[index]
            if self._history_windows.get(webengineview):
                del self._history_windows[webengineview]
            self._webengineviews.remove(webengineview)
            self.removeTab(index)

    def close_current_tab(self):
        self.handle_tab_close_request(self.currentIndex())

    def _trigger_action(self, action):
        index = self.currentIndex()
        if index >= 0:
            self._webengineviews[index].page().triggerAction(action)

    def _index_of_page(self, web_page):
        for p in range(0, len(self._webengineviews)):
            if (self._webengineviews[p].page() == web_page):
                return p
        return -1

    def _download_requested(self, item):
        self.download_requested.emit(item)


_url_role = Qt.UserRole + 1

# Default bookmarks as an array of arrays which is the form
# used to read from/write to a .json bookmarks file
_default_bookmarks = [
    ['Tool Bar'],
]


def _config_dir():
    return '{}/QtForPythonBrowser'.format(
        QStandardPaths.writableLocation(QStandardPaths.ConfigLocation))


_bookmark_file = 'bookmarks.json'


def _create_folder_item(title):
    result = QStandardItem(title)
    result.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
    return result


def _create_item(url, title, icon):
    result = QStandardItem(title)
    result.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
    result.setData(url, _url_role)
    if icon is not None:
        result.setIcon(icon)
    return result


# Create the model from an array of arrays
def _create_model(parent, serialized_bookmarks):
    result = QStandardItemModel(0, 1, parent)
    last_folder_item = None
    for entry in serialized_bookmarks:
        if len(entry) == 1:
            last_folder_item = _create_folder_item(entry[0])
            result.appendRow(last_folder_item)
        else:
            url = QUrl.fromUserInput(entry[0])
            title = entry[1]
            icon = QIcon(entry[2]) if len(entry) > 2 and entry[2] else None
            last_folder_item.appendRow(_create_item(url, title, icon))
    return result


# Serialize model into an array of arrays, writing out the icons
# into .png files under directory in the process
def _serialize_model(model, directory):
    result = []
    folder_count = model.rowCount()
    for f in range(0, folder_count):
        folder_item = model.item(f)
        result.append([folder_item.text()])
        item_count = folder_item.rowCount()
        for i in range(0, item_count):
            item = folder_item.child(i)
            entry = [item.data(_url_role).toString(), item.text()]
            icon = item.icon()
            if not icon.isNull():
                icon_sizes = icon.availableSizes()
                largest_size = icon_sizes[len(icon_sizes) - 1]
                icon_file_name = '{}/icon{:02}_{:02}_{}.png'.format(directory,
                                                                    f, i,
                                                                    largest_size.width())
                icon.pixmap(largest_size).save(icon_file_name, 'PNG')
                entry.append(icon_file_name)
            result.append(entry)
    return result


# Bookmarks as a tree view to be used in a dock widget with
# functionality to persist and populate tool bars and menus.
class BookmarkWidget(QTreeView):
    """Provides a tree view to manage the bookmarks."""

    open_bookmark = QtCore.Signal(QUrl)
    open_bookmark_in_new_tab = QtCore.Signal(QUrl)
    changed = QtCore.Signal()

    def __init__(self):
        super(BookmarkWidget, self).__init__()
        self.setRootIsDecorated(False)
        self.setUniformRowHeights(True)
        self.setHeaderHidden(True)
        self._model = _create_model(self, self._read_bookmarks())
        self.setModel(self._model)
        self.expandAll()
        self.activated.connect(self._activated)
        self._model.rowsInserted.connect(self._changed)
        self._model.rowsRemoved.connect(self._changed)
        self._model.dataChanged.connect(self._changed)
        self._modified = False
        self.customContextMenuRequested.connect(self.context_menu_event)

    def _changed(self):
        self._modified = True
        self.changed.emit()

    def _activated(self, index):
        item = self._model.itemFromIndex(index)
        self.open_bookmark.emit(item.data(_url_role))

    def _action_activated(self, index):
        action = self.sender()
        self.open_bookmark.emit(action.data())

    def _tool_bar_item(self):
        return self._model.item(0, 0)

    def _other_item(self):
        return self._model.item(1, 0)

    def add_bookmark(self, url, title, icon):
        self._other_item().appendRow(_create_item(url, title, icon))

    def add_tool_bar_bookmark(self, url, title, icon):
        self._tool_bar_item().appendRow(_create_item(url, title, icon))

    # Synchronize the bookmarks under parent_item to a target_object
    # like QMenu/QToolBar, which has a list of actions. Update
    # the existing actions, append new ones if needed or hide
    # superfluous ones
    def _populate_actions(self, parent_item, target_object, first_action):
        existing_actions = target_object.actions()
        existing_action_count = len(existing_actions)
        a = first_action
        row_count = parent_item.rowCount()
        for r in range(0, row_count):
            item = parent_item.child(r)
            title = item.text()
            icon = item.icon()
            url = item.data(_url_role)
            if a < existing_action_count:
                action = existing_actions[a]
                if (title != action.toolTip()):
                    action.setText(BookmarkWidget.short_title(title))
                    action.setIcon(icon)
                    action.setToolTip(title)
                    action.setData(url)
                    action.setVisible(True)
            else:
                short_title = BookmarkWidget.short_title(title)
                action = target_object.addAction(icon, short_title)
                action.setToolTip(title)
                action.setData(url)
                action.triggered.connect(self._action_activated)
            a = a + 1
        while a < existing_action_count:
            existing_actions[a].setVisible(False)
            a = a + 1

    def populate_tool_bar(self, tool_bar):
        self._populate_actions(self._tool_bar_item(), tool_bar, 0)

    def populate_other(self, menu, first_action):
        self._populate_actions(self._other_item(), menu, first_action)

    def _current_item(self):
        index = self.currentIndex()
        if index.isValid():
            item = self._model.itemFromIndex(index)
            if item.parent():  # exclude top level items
                return item
        return None

    def context_menu_event(self, event):
        context_menu = QMenu()
        open_in_new_tab_action = context_menu.addAction("Open in New Tab")
        remove_action = context_menu.addAction("Remove...")
        current_item = self._current_item()
        open_in_new_tab_action.setEnabled(current_item is not None)
        remove_action.setEnabled(current_item is not None)
        chosen_action = context_menu.exec_(event.globalPos())
        if chosen_action == open_in_new_tab_action:
            self.open_bookmarkInNewTab.emit(current_item.data(_url_role))
        elif chosen_action == remove_action:
            self._remove_item(current_item)

    def _remove_item(self, item):
        message = "Would you like to remove \"{}\"?".format(item.text())
        button = QMessageBox.question(self, "Remove", message,
                                      QMessageBox.Yes | QMessageBox.No)
        if button == QMessageBox.Yes:
            item.parent().removeRow(item.row())

    def write_bookmarks(self):
        if not self._modified:
            return
        dir_path = _config_dir()
        native_dir_path = QDir.toNativeSeparators(dir_path)
        dir = QFileInfo(dir_path)
        if not dir.isDir():
            if not QDir(dir.absolutePath()).mkpath(dir.fileName()):
                warnings.warn('Cannot create {}.'.format(native_dir_path),
                              RuntimeWarning)
                return
        serialized_model = _serialize_model(self._model, dir_path)
        bookmark_file_name = os.path.join(native_dir_path, _bookmark_file)
        with open(bookmark_file_name, 'w') as bookmark_file:
            json.dump(serialized_model, bookmark_file, indent=4)

    def _read_bookmarks(self):
        bookmark_file_name = os.path.join(QDir.toNativeSeparators(_config_dir()),
                                          _bookmark_file)
        if os.path.exists(bookmark_file_name):
            return json.load(open(bookmark_file_name))
        return _default_bookmarks

    # Return a short title for a bookmark action,
    # "Qt | Cross Platform.." -> "Qt"
    @staticmethod
    def short_title(t):
        i = t.find(' | ')
        if i == -1:
            i = t.find(' - ')
        return t[0:i] if i != -1 else t



main_windows = []

cwd = os.getcwd()
DYNOBITEFILES = "Dynobite Files"
DynobiteCreateFolder = os.path.join(cwd, DYNOBITEFILES)
DynobiteHistoryFolder = os.path.join(DYNOBITEFILES, "History.txt")

print("Dynobite\nVersion 94.0.992.31")

try:
    os.mkdir(DynobiteCreateFolder)
except FileExistsError:
    pass

picturefolder = "Images"
completedir = os.path.join(DynobiteCreateFolder, picturefolder)

def download(fullurl, downloadname):
        import os
        import requests

        from urllib.parse import urlparse
        from pathlib import Path

        a = urlparse(fullurl)
        fn=downloadname

        if os.path.isfile(fn):
            print('Skipping download, file exists {0}'.format(fn))
        else:
            print('Downloading file {0}'.format(fn))
            r=requests.get(fullurl, stream=True)
            with open(fn,'wb') as f:
                f.write(r.content)

try:
    os.mkdir(completedir)
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/1.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/1.png')

except FileExistsError:
    pass

def create_main_window():
    """Creates a MainWindow using 75% of the available screen resolution."""
    main_win = MainWindow()
    main_windows.append(main_win)
    available_geometry = app.desktop().availableGeometry(main_win)
    main_win.resize(available_geometry.width() * 2 / 3,
                    available_geometry.height() * 2 / 3)
    main_win.show()
    return main_win


def create_main_window_with_browser():
    """Creates a MainWindow with a BrowserTabWidget."""
    main_win = create_main_window()
    return main_win.add_browser_tab()

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(os.path.join(completedir, '1.png')))
        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Dynobite - The Browser that is 2x Faster")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join(completedir, '1.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Built by Abhinav Satheesh"))
        layout.addWidget(QLabel("https://abhinavsatheesh.github.dyn.com/"))
        layout.addWidget(QLabel("GitHub Repository Link - https://github.com/abhinavsatheesh/dynfiles"))
        layout.addWidget(QLabel("Version 94.0.992.31"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)      


class MainWindow(QMainWindow):
    """Provides the parent window that includes the BookmarkWidget,
    BrowserTabWidget, and a DownloadWidget, to offer the complete
    web browsing experience."""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Dynobite')

        self._tab_widget = BrowserTabWidget(create_main_window_with_browser)
        self._tab_widget.enabled_changed.connect(self._enabled_changed)
        self._tab_widget.download_requested.connect(self._download_requested)
        self.setCentralWidget(self._tab_widget)
        self.connect(self._tab_widget, QtCore.SIGNAL("url_changed(QUrl)"),
                     self.url_changed)

        self._bookmark_dock = QDockWidget()
        self._bookmark_dock.setWindowTitle('Bookmarks')
        self._bookmark_widget = BookmarkWidget()
        self._bookmark_widget.open_bookmark.connect(self.load_url)
        self._bookmark_widget.open_bookmark_in_new_tab.connect(self.load_url_in_new_tab)
        self._bookmark_dock.setWidget(self._bookmark_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self._bookmark_dock)
        self.setWindowIcon(QIcon(os.path.join(completedir, '1.png')))
        self._find_tool_bar = None
        self._bookmark_dock.customContextMenuRequested.connect(self.context_menu_event)

        # self.view = QtWebEngineWidgets.QWebEngineView()

        self._actions = {}
        self._create_menu()

        self._tool_bar = QToolBar()
        self.addToolBar(self._tool_bar)
        for action in self._actions.values():
            if not action.icon().isNull():
                self._tool_bar.addAction(action)

        self._addres_line_edit = QLineEdit()
        self._addres_line_edit.setClearButtonEnabled(True)
        self._addres_line_edit.returnPressed.connect(self.load)
        self._tool_bar.addWidget(self._addres_line_edit)
        self._zoom_label = QLabel()
        self.statusBar().addPermanentWidget(self._zoom_label)
        self._update_zoom_label()
        self._bookmarksToolBar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self._bookmarksToolBar)
        self.insertToolBarBreak(self._bookmarksToolBar)
        self._bookmark_widget.changed.connect(self._update_bookmarks)

        self.page = QWebEnginePage()

    def context_menu_event(self, event):
        context_menu = QMenu()
        open_in_new_tab_action = context_menu.addAction("Open in New Tab")
        remove_action = context_menu.addAction("Remove...")
        current_item = self._current_item()
        open_in_new_tab_action.setEnabled(current_item is not None)
        remove_action.setEnabled(current_item is not None)
        chosen_action = context_menu.exec_(event.globalPos())
        if chosen_action == open_in_new_tab_action:
            self.open_bookmarkInNewTab.emit(current_item.data(_url_role))
        elif chosen_action == remove_action:
            self._remove_item(current_item)

    def _update_bookmarks(self):
        self._bookmark_widget.populate_tool_bar(self._bookmarksToolBar)
        self._bookmark_widget.populate_other(self._bookmark_menu, 3)

    def _create_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        new_tab_action = QAction("New Tab", self,
                                 shortcut='Ctrl+T',
                                 triggered=self.add_browser_tab)
        file_menu.addAction(new_tab_action)
        new_window_action = QAction("New Window", self,
                                 shortcut='Ctrl+N',
                                 triggered=self.OPEN_NEW_WINDOW)
        file_menu.addAction(new_window_action)
        close_tab_action = QAction("Close Tab", self,
                                   shortcut="Ctrl+W",
                                   triggered=self._close_current_tab)
        file_menu.addAction(close_tab_action)
        new_window_action = QAction("Open File", self,
                                 shortcut='Ctrl+O',
                                 triggered=self.open_file)
        file_menu.addAction(new_window_action)
        exit_action = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                              self, shortcut="Ctrl+Q", triggered=qApp.quit)
        file_menu.addAction(exit_action)

        navigation_menu = self.menuBar().addMenu("&Navigation")

        style_icons = ':/qt-project.org/styles/commonstyle/images/'
        back_action = QAction(QIcon.fromTheme("go-previous",
                                              QIcon(style_icons + 'left-32.png')),
                              "Back", self,
                              shortcut=QKeySequence(QKeySequence.Back),
                              triggered=self._tab_widget.back)
        self._actions[QWebEnginePage.Back] = back_action
        back_action.setEnabled(False)
        navigation_menu.addAction(back_action)
        forward_action = QAction(QIcon.fromTheme("go-next",
                                                 QIcon(style_icons + 'right-32.png')),
                                 "Forward", self,
                                 shortcut=QKeySequence(QKeySequence.Forward),
                                 triggered=self._tab_widget.forward)
        forward_action.setEnabled(False)
        self._actions[QWebEnginePage.Forward] = forward_action

        navigation_menu.addAction(forward_action)
        reload_action = QAction(QIcon(style_icons + 'refresh-32.png'),
                                "Reload", self,
                                shortcut=QKeySequence(QKeySequence.Refresh),
                                triggered=self._tab_widget.reload)
        self._actions[QWebEnginePage.Reload] = reload_action
        reload_action.setEnabled(False)
        navigation_menu.addAction(reload_action)

        navigation_menu.addSeparator()

        mute_action = QAction("Mute Tab", self,
                                   shortcut="Ctrl+M",
                                   triggered=self.MUTETAB)
        navigation_menu.addAction(mute_action)

        navigation_menu.addSeparator()

        

        edit_menu = self.menuBar().addMenu("&Edit")

        find_action = QAction("Find", self,
                              shortcut=QKeySequence(QKeySequence.Find),
                              triggered=self._show_find)
        edit_menu.addAction(find_action)

        edit_menu.addSeparator()
        undo_action = QAction("Undo", self,
                              shortcut=QKeySequence(QKeySequence.Undo),
                              triggered=self._tab_widget.undo)
        self._actions[QWebEnginePage.Undo] = undo_action
        undo_action.setEnabled(False)
        edit_menu.addAction(undo_action)

        redo_action = QAction("Redo", self,
                              shortcut=QKeySequence(QKeySequence.Redo),
                              triggered=self._tab_widget.redo)
        self._actions[QWebEnginePage.Redo] = redo_action
        redo_action.setEnabled(False)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction("Cut", self,
                             shortcut=QKeySequence(QKeySequence.Cut),
                             triggered=self._tab_widget.cut)
        self._actions[QWebEnginePage.Cut] = cut_action
        cut_action.setEnabled(False)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Copy", self,
                              shortcut=QKeySequence(QKeySequence.Copy),
                              triggered=self._tab_widget.copy)
        self._actions[QWebEnginePage.Copy] = copy_action
        copy_action.setEnabled(False)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self,
                               shortcut=QKeySequence(QKeySequence.Paste),
                               triggered=self._tab_widget.paste)
        self._actions[QWebEnginePage.Paste] = paste_action
        paste_action.setEnabled(False)
        edit_menu.addAction(paste_action)

        edit_menu.addSeparator()

        select_all_action = QAction("Select All", self,
                                    shortcut=QKeySequence(QKeySequence.SelectAll),
                                    triggered=self._tab_widget.select_all)
        self._actions[QWebEnginePage.SelectAll] = select_all_action
        select_all_action.setEnabled(False)
        edit_menu.addAction(select_all_action)

        self._bookmark_menu = self.menuBar().addMenu("&Bookmarks")
        add_tool_bar_bookmark_action = QAction("&Add Bookmark", self,
                                              shortcut="Ctrl+D",
                                               triggered=self._add_tool_bar_bookmark)
        self._bookmark_menu.addAction(add_tool_bar_bookmark_action)
        self._bookmark_menu.addSeparator()

        tools_menu = self.menuBar().addMenu("&Tools")
        download_action = QAction("Open Downloads", self,
                                  shortcut="Ctrl+J",
                                  triggered=DownloadWidget.open_download_directory)
        tools_menu.addAction(download_action)
        history_action = QAction("History", self,
                                 shortcut="Ctrl+H",
                                 triggered=self._tab_widget.show_history)
        tools_menu.addAction(history_action)

        window_menu = self.menuBar().addMenu("&Window")

        window_menu.addAction(self._bookmark_dock.toggleViewAction())

        window_menu.addSeparator()

        zoom_in_action = QAction(QIcon.fromTheme("zoom-in"),
                                 "Zoom In", self,
                                 shortcut=QKeySequence(QKeySequence.ZoomIn),
                                 triggered=self._zoom_in)
        window_menu.addAction(zoom_in_action)
        zoom_out_action = QAction(QIcon.fromTheme("zoom-out"),
                                  "Zoom Out", self,
                                  shortcut=QKeySequence(QKeySequence.ZoomOut),
                                  triggered=self._zoom_out)
        window_menu.addAction(zoom_out_action)

        reset_zoom_action = QAction(QIcon.fromTheme("zoom-original"),
                                    "Reset Zoom", self,
                                    shortcut="Ctrl+0",
                                    triggered=self._reset_zoom)
        window_menu.addAction(reset_zoom_action)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "PDF Files (*.pdf);;"
                                                  "All files (*.*)")

        
        split_tup = os.path.splitext(filename)
        file_extension = split_tup[1]
        if file_extension==".pdf":
            root = Tk()
            root.title("PDF Viewer") 
  
            root.geometry("550x750") 
            
            v1 = pdf.ShowPdf() 
            
            v2 = v1.pdf_view(root, 
                            pdf_location = filename,  
                            width = 750, height = 100) 
            
            v2.pack() 
            root.mainloop()
            self._addres_line_edit.setText(filename)

    def MUTETAB(self):
        self.page.setAudioMuted(True)
    
    def add_browser_tab(self):
        return self._tab_widget.add_browser_tab()
        QWebEnginePage.setUrl("https://www.google.com")

    def _close_current_tab(self):
        if self._tab_widget.count() > 1:
            self._tab_widget.close_current_tab()
        else:
            self.close()

    def print_page(self):
        dlg = QPrintDialog(self.printer)
        if dlg.exec_():
            self.browser.page().print(self.printer, self.print_completed)

    def print_completed(self, success):
        pass


    def OPEN_NEW_WINDOW(self):
        create_main_window_with_browser()

    def closeEvent(self, event):
        if self._tab_widget.count() > 1:
            reply = QMessageBox.question(self, 'Close all tabs?', f'You have {self._tab_widget.count()} tabs open', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()      
        else:
            self.close()

    def load(self):
        url_string = self._addres_line_edit.text().strip()
        if validators.url(url_string):
            q = QUrl(url_string)
            justurl = str(q)
            firsttime = justurl.split("PySide2.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)
        elif validators.url(f"https://{url_string}"):
            q = QUrl(f"http://{url_string}")
            justurl = str(q)
            firsttime = justurl.split("PySide2.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        elif url_string.find("file:///") == 0 or url_string.find("view-source:") == 0 :
            q = QUrl(url_string)
            justurl = str(q)
            firsttime = justurl.split("PySide2.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        else:
            url = f'https://www.google.com/search?q={url_string.replace("+","%2B").replace(" ","+")}'
            q = QUrl(url)
            justurl = str(q)
            firsttime = justurl.split("PySide2.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        self.load_url_string(urlfinal)

    def load_url_string(self, url_s):
        url = QUrl.fromUserInput(url_s)
        if (url.isValid()):
            self.load_url(url)

    def load_url(self, url):
        self._tab_widget.load(url)

    def load_url_in_new_tab(self, url):
        self.add_browser_tab().load(url)

    def url_changed(self, url):
        self._addres_line_edit.setText(url.toString())

    def _enabled_changed(self, web_action, enabled):
        action = self._actions[web_action]
        if action:
            action.setEnabled(enabled)

    def _add_bookmark(self):
        index = self._tab_widget.currentIndex()
        if index >= 0:
            url = self._tab_widget.url()
            title = self._tab_widget.tabText(index)
            icon = self._tab_widget.tabIcon(index)
            self._bookmark_widget.add_bookmark(url, title, icon)

    def _add_tool_bar_bookmark(self):
        index = self._tab_widget.currentIndex()
        if index >= 0:
            url = self._tab_widget.url()
            title = self._tab_widget.tabText(index)
            icon = self._tab_widget.tabIcon(index)
            self._bookmark_widget.add_tool_bar_bookmark(url, title, icon)

    def _zoom_in(self):
        new_zoom = self._tab_widget.zoom_factor() * 1.5
        if (new_zoom <= WebEngineView.maximum_zoom_factor()):
            self._tab_widget.set_zoom_factor(new_zoom)
            self._update_zoom_label()

    def _zoom_out(self):
        new_zoom = self._tab_widget.zoom_factor() / 1.5
        if (new_zoom >= WebEngineView.minimum_zoom_factor()):
            self._tab_widget.set_zoom_factor(new_zoom)
            self._update_zoom_label()

    def _reset_zoom(self):
        self._tab_widget.set_zoom_factor(1)
        self._update_zoom_label()

    def _update_zoom_label(self):
        percent = int(self._tab_widget.zoom_factor() * 100)
        self._zoom_label.setText("{}%".format(percent))

    def _download_requested(self, item):
        # Remove old downloads before opening a new one
        for old_download in self.statusBar().children():
            if (type(old_download).__name__ == 'DownloadWidget' and
                old_download.state() != QWebEngineDownloadItem.DownloadInProgress):
                self.statusBar().removeWidget(old_download)
                del old_download

        item.accept()
        download_widget = DownloadWidget(item)
        download_widget.remove_requested.connect(self._remove_download_requested,
                                                 Qt.QueuedConnection)
        self.statusBar().addWidget(download_widget)

    def _remove_download_requested(self):
            download_widget = self.sender()
            self.statusBar().removeWidget(download_widget)
            del download_widget

    def _show_find(self):
        if self._find_tool_bar is None:
            self._find_tool_bar = FindToolBar()
            self._find_tool_bar.find.connect(self._tab_widget.find)
            self.addToolBar(Qt.BottomToolBarArea, self._find_tool_bar)
        else:
            self._find_tool_bar.show()
        self._find_tool_bar.focus_find()

    def write_bookmarks(self):
        self._bookmark_widget.write_bookmarks()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = create_main_window()
    initial_urls = sys.argv[1:]
    if not initial_urls:
        initial_urls.append('https://www.google.com')
    for url in initial_urls:
        main_win.load_url_in_new_tab(QUrl.fromUserInput(url))
    exit_code = app.exec_()
    main_win.write_bookmarks()
    sys.exit(exit_code)
