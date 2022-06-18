from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtPrintSupport
from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog as fd 
import os
import sys
import pyperclip as pc
import random
import validators
import webbrowser
import mimetypes
import requests
import threading
import json
import favicon
import time
import pyautogui

#Version = Version 7
print("Dynobite\nVersion 7")  
  
cwd = os.getcwd()
DYNOBITEFILES = "Dynobite Files"
DynobiteCreateFolder = os.path.join(cwd, DYNOBITEFILES)
DynobiteHistoryFolder = os.path.join(DYNOBITEFILES, "History.txt")

try:
    os.mkdir(DynobiteCreateFolder)
except FileExistsError:
    pass

screenshotfolder = "Screenshots"
picturefolder = "Images"
downloadfolder = "Downloads"
completedir = os.path.join(DynobiteCreateFolder, picturefolder)
completedownloaddir = os.path.join(DynobiteCreateFolder, downloadfolder)
completescreendir = os.path.join(DynobiteCreateFolder, screenshotfolder)

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
    os.mkdir(completedownloaddir)
    os.mkdir(completescreendir)
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_back.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_back.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_close.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_close.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_forward.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_forward.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_history.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_history.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_home.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_home.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_newprivate.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_newprivate.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_newtabpage.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_newtabpage.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_newwindow.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_newwindow.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_openfile.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_openfile.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_pagesource.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_pagesource.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_reload.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_reload.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_screenshot.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_screenshot.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/favicon_translate.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/favicon_translate.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/lifebuoy.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/lifebuoy.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/1.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/1.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/question.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/question.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/shield.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/shield.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/signal.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/signal.png')
    url="https://raw.githubusercontent.com/abhinavsatheesh/dynfiles/main/Dynobite/Images/games.png"
    downloadpath=completedir
    download(url,f'{downloadpath}/games.png')

except FileExistsError:
    pass



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
        layout.addWidget(QLabel("Version 7"))
        layout.addWidget(QLabel("Copyright 2021 Dyn Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)      

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def __init__(self, parent=None):
        super(WebEnginePage, self).__init__(parent)
        self.featurePermissionRequested.connect(
            self.handleFeaturePermissionRequested)

    @QtCore.pyqtSlot(QtCore.QUrl, QtWebEngineWidgets.QWebEnginePage.Feature)
    def handleFeaturePermissionRequested(self, securityOrigin, feature):
        title = "Permission Request"
        questionForFeature = {
            QtWebEngineWidgets.QWebEnginePage.Geolocation: "Allow {feature} to access your location information?",
            QtWebEngineWidgets.QWebEnginePage.MediaAudioCapture: "Allow {feature} to access your microphone?",
            QtWebEngineWidgets.QWebEnginePage.MediaVideoCapture: "Allow {feature} to access your webcam?",
            QtWebEngineWidgets.QWebEnginePage.MediaAudioVideoCapture: "Allow {feature} to lock your mouse cursor?",
            QtWebEngineWidgets.QWebEnginePage.DesktopVideoCapture: "Allow {feature} to capture video of your desktop?",
            QtWebEngineWidgets.QWebEnginePage.DesktopAudioVideoCapture: "Allow {feature} to capture audio and video of your desktop?"
        }
        question = questionForFeature.get(feature)
        if question:
            question = question.format(feature=securityOrigin.host())
            if QtWidgets.QMessageBox.question(self.view().window(), title, question) == QtWidgets.QMessageBox.Yes:
                self.setFeaturePermission(
                    securityOrigin, feature, QtWebEngineWidgets.QWebEnginePage.PermissionGrantedByUser)
            else:
                self.setFeaturePermission(
                    securityOrigin, feature, QtWebEngineWidgets.QWebEnginePage.PermissionDeniedByUser)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab) 
        self.zoom_factor = 2        
        
        self.setCentralWidget(self.tabs)
        
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(32, 32))
        navtb.setMovable(False)
        self.addToolBar(navtb)
        

        back_btn = QAction(QIcon(os.path.join(completedir, 'favicon_back.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join(completedir, 'favicon_forward.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join(completedir, 'favicon_reload.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        stop_btn = QAction(QIcon(os.path.join(completedir, 'favicon_close.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        home_btn = QAction(QIcon(os.path.join(completedir, 'favicon_home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        newtab_btn = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "New Tab", self)
        newtab_btn.setStatusTip("Open a new tab")
        newtab_btn.triggered.connect(lambda _: self.add_new_tab())
        navtb.addAction(newtab_btn)        

        navtb.addSeparator()

        self.httpsicon = QLabel()  
        self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'shield.png')))
        navtb.addWidget(self.httpsicon)      
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setFixedHeight(28)
        navtb.addWidget(self.urlbar)

        navtb.setStyleSheet("""
                                QToolBar {
                                    background-color: #ffffff; 
                                    color:#000000;
                                }
                                QToolBar QToolButton {
                                    background-color: #ffffff;
                                    border-radius: 2px;
                                }
                                QToolBar QToolButton:pressed {
                                    background-color: #AAB0BC;
                                    border-radius: 2px;
                                }
                                
                                """)
        self.tabs.setStyleSheet("""
                                    QTabWidget {
                                        background: #ffffff; 
                                    }
                                    QTabBar {
                                        background: #e7eaed; 
                                    }
                                    QTabBar::tab {
                                        background: #e7eaed; 
                                        padding: 10px;
                                        color: #000000;
                                        margin-top: -1px;
                                        margin-bottom: -1px; 
                                        margin-left: 1pt solid black;
                                        margin-right: 1pt solid black;
                                        border: 1px solid #000000;
                                        border-radius: 4px;
                                    } 
                                    QTabBar::tab:hover { 
                                        background: #f0f0f0;  
                                    } 
                                    QTabBar::tab:selected { 
                                        background: #ffffff;  
                                        color: #000000;
                                    }
                                    """)
        self.urlbar.setStyleSheet(
               "font-size: 10pt;border: 1px solid #0088ff;border-radius: 5px;background-color:#ffffff;color:#000000")
        
        navtb.addSeparator()
        
        btn = QPushButton(':', self)
        btn.resize(32, 32)
        menu = QMenu()
        menu.triggered.connect(lambda x: print(x.text()))
        btn.setMenu(menu)
        btn.setStyleSheet(
               "font-size: 10pt;border: 1px solid #0088ff;border-radius: 5px;background-color:#ffffff;color:#000000")
        
        navtb.addWidget(btn)      
        
        new_tab_action = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        menu.addAction(new_tab_action)
        
        new_window_action = QAction(QIcon(os.path.join(completedir, 'favicon_newwindow.png')), "New Window", self)
        new_window_action.setStatusTip("Open a new window")
        new_window_action.triggered.connect(lambda _: self.addnewwindow())
        menu.addAction(new_window_action)
        
        new_privatewindow_action = QAction(QIcon(os.path.join(completedir, 'favicon_newprivate.png')), "New PrivateBrowse Window", self)
        new_privatewindow_action.setStatusTip("Open a new PrivateBrowse window")
        new_privatewindow_action.triggered.connect(lambda _: self.givealert())
        menu.addAction(new_privatewindow_action)
        
        duplicate_tab_action = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "Duplicate Tab", self)
        duplicate_tab_action.setStatusTip("Duplicate Tab")
        duplicate_tab_action.triggered.connect(self.DUPLICATETAB)
        menu.addAction(duplicate_tab_action)
        
        menu.addSeparator()
        
        open_file_action = QAction(QIcon(os.path.join(completedir, 'favicon_openfile.png')), "Open File", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        menu.addAction(open_file_action)
        
        save_file_action = QAction(QIcon(os.path.join('images', 'favicon_savepage.png')), "Save Page", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        menu.addAction(save_file_action)

        print_file_action = QAction(QIcon(os.path.join('images', 'favicon_savepage.png')), "Print Page", self)
        print_file_action.setStatusTip("Print current page")
        print_file_action.triggered.connect(self.printRequested)
        menu.addAction(print_file_action)
      
        history_action = QAction(QIcon(os.path.join(completedir, 'favicon_history.png')), "History", self)
        history_action.setStatusTip("View Browsing History")
        history_action.triggered.connect(self.OPENHISTORY)
        menu.addAction(history_action)

        clear_history = QAction(QIcon(os.path.join(completedir, 'favicon_history.png')), "Clear History", self)
        clear_history.setStatusTip("Clear Browsing History")
        clear_history.triggered.connect(self.CLEARHISTORY)
        menu.addAction(clear_history)
        
        downloadbutton_action = QAction(QIcon(os.path.join(completedir, 'favicon_downloads.png')), "Downloads", self)
        downloadbutton_action.setStatusTip("Open Downloads Folder")
        downloadbutton_action.triggered.connect(self.OPENDOWNLOADS)
        menu.addAction(downloadbutton_action)
        
        menu.addSeparator()
        
        screenshot_btn = QAction(QIcon(os.path.join(completedir, 'favicon_screenshot.png')), "Screenshot", self)
        screenshot_btn.setStatusTip("Capture Screenshot")
        screenshot_btn.triggered.connect(lambda:self.screenshot())
        menu.addAction(screenshot_btn)
        
        view_source = QAction(QIcon(os.path.join(completedir, 'favicon_pagesource.png')), "View Page Source", self)
        view_source.setStatusTip("View Page Source")
        view_source.triggered.connect(self.viewpage)
        menu.addAction(view_source)
        
        impMenu = QMenu('Share', self)
        
        link_share = QAction(QIcon(os.path.join(completedir, 'favicon_copylink.png')),'Copy Link', self)
        link_share.triggered.connect(self.copytext)
        impMenu.addAction(link_share)
        
        qr_share = QAction(QIcon(os.path.join(completedir, 'favicon_copylink.png')),'Generate QR Code', self)
        qr_share.triggered.connect(self.QR_CODE)
        impMenu.addAction(qr_share)
        
        share_with_whatsapp = QAction(QIcon(os.path.join(completedir, 'favicon_whatsapp.png')),'Share with WhatsApp', self)
        share_with_whatsapp.triggered.connect(self.SHARE_WITH_WHATSAPP)
        impMenu.addAction(share_with_whatsapp)
        
        share_with_gmail = QAction(QIcon(os.path.join(completedir, 'favicon_gmail.png')),'Share with Gmail', self)
        share_with_gmail.triggered.connect(self.SHARE_WITH_GMAIL)
        impMenu.addAction(share_with_gmail)

        menu.addMenu(impMenu)
       
        translate_action = QAction(QIcon(os.path.join(completedir, 'favicon_translate.png')), "Translate Page", self)
        translate_action.setStatusTip("Translate the current page")
        translate_action.triggered.connect(self.TRANSLATEPAGE)
        menu.addAction(translate_action)
        
        menu.addSeparator()

        game_surf_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Surf", self)        
        game_surf_action.setStatusTip("Play Surf")
        game_surf_action.triggered.connect(self.EDGESURF)
        menu.addAction(game_surf_action)

        game_dino_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Dino", self)        
        game_dino_action.setStatusTip("Play Dino")
        game_dino_action.triggered.connect(self.CHROMEDINO)
        menu.addAction(game_dino_action)   

        game_slitheraction = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Slither", self)        
        game_slitheraction.setStatusTip("Play Slither")
        game_slitheraction.triggered.connect(self.FIREFOXSLITHER)
        menu.addAction(game_slitheraction)
        
        game_shell_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Shell Shocker", self)        
        game_shell_action.setStatusTip("Play Shell Shocker")
        game_shell_action.triggered.connect(self.SHELLSHOCK)
        menu.addAction(game_shell_action)
        
        menu.addSeparator()
        
        about_action = QAction(QIcon(os.path.join(completedir, 'question.png')), "About Dynobite", self)
        about_action.setStatusTip("Find out more about Dynobite")
        about_action.triggered.connect(self.about)
        menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join(completedir, 'favicon_home.png')),
                                            "Dynobite Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Dynobite Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        menu.addAction(navigate_mozarella_action)
        
        URL = "https://www.google.co.in"
        self.add_new_tab(QUrl(URL), 'Homepage')
        self.NewTabListener = QShortcut(QKeySequence('Ctrl+T'), self)
        self.NewTabListener.activated.connect(lambda : self.add_new_tab())
        self.NewWindowListener = QShortcut(QKeySequence('Ctrl+N'), self)
        self.NewWindowListener.activated.connect(lambda : self.addnewwindow())
        self.PrivateWindowListener = QShortcut(QKeySequence('Ctrl+Shift+N'), self)
        self.PrivateWindowListener.activated.connect(lambda : self.givealert())
        self.HistoryListener = QShortcut(QKeySequence('Ctrl+H'), self)
        self.HistoryListener.activated.connect(lambda : self.OPENHISTORY())
        self.ClearHistoryListener = QShortcut(QKeySequence('Ctrl+Shift+Del'), self)
        self.ClearHistoryListener.activated.connect(lambda : self.CLEARHISTORY())
        self.DuplicateTabListener = QShortcut(QKeySequence('Ctrl+K'), self)
        self.DuplicateTabListener.activated.connect(lambda : self.DUPLICATETAB())
        self.OpenFileListener = QShortcut(QKeySequence('Ctrl+O'), self)
        self.OpenFileListener.activated.connect(lambda : self.open_file())
        self.SaveFileListener = QShortcut(QKeySequence('Ctrl+S'), self)
        self.SaveFileListener.activated.connect(lambda : self.save_file())
        self.ScreenshotListener = QShortcut(QKeySequence('Ctrl+Shift+S'), self)
        self.ScreenshotListener.activated.connect(lambda : self.screenshot())
        self.ViewSourceListener = QShortcut(QKeySequence('Ctrl+U'), self)
        self.ViewSourceListener.activated.connect(lambda : self.viewpage())
        self.DownloadListener = QShortcut(QKeySequence('Ctrl+J'), self)
        self.DownloadListener.activated.connect(lambda : self.OPENDOWNLOADS())
        self.ReloadListener = QShortcut(QKeySequence("Ctrl+R"), self)
        self.ReloadListener.activated.connect(lambda : self.tabs.currentWidget().reload())
        self.ReloadListener1 = QShortcut(QKeySequence("F5"), self)
        self.ReloadListener1.activated.connect(lambda : self.tabs.currentWidget().reload())

        self.menuBar().setNativeMenuBar(False)
        self.show()
        self.setWindowTitle("Dynobite")
        self.setWindowIcon(QIcon(os.path.join(completedir, '1.png')))
            
    def closeEvent(self, event):
        if self.tabs.count() > 1:
            reply = QMessageBox.question(self, 'Close all tabs?', f'You have {self.tabs.count()} tabs open', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()      
        else:
            self.close()
   
    def OPENDOWNLOADS(self):
        os.startfile(completedownloaddir)
        
    def printRequested(self):
            # if you are viewing this part of my code can you please improve this as I don't think this is the best way to print a page and I can't understand how to fix this
            url = self.urlbar.text()
            if url == "":
                url = 'file:///html/home.html'
            self.view = QtWebEngineWidgets.QWebEngineView()
            self.page = QtWebEngineWidgets.QWebEnginePage(self)
            self.view.setPage(self.page)
            self.view.load(QtCore.QUrl(url))
            defaultPrinter = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinterInfo.defaultPrinter())
            dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
            if dialog.exec():
                # printer object has to be persistent
                self._printer = dialog.printer()
                self.page.print(self._printer, self.printResult)

    def printResult(self, success):
        if success:
            pass
        else:
            QtWidgets.QMessageBox.information(self, 'Print failed',
                                                 'Printing has failed!', QtWidgets.QMessageBox.Ok)
        del self._printer
      
    def SHELLSHOCK(self):
        self.add_new_tab(qurl="https://shellshock.io/")
        site = "https://shellshock.io/"
        self.urlbar.setText(site)
        try:
            towrite = f"\n {site}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass
    
    def EDGESURF(self):
        self.add_new_tab(qurl="https://surf.jackbuehner.com/")
        site = "https://surf.jackbuehner.com/"
        self.urlbar.setText(site)
        try:
            towrite = f"\n {site}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass

    def CHROMEDINO(self):
        self.add_new_tab(qurl="http://wayou.github.io/t-rex-runner/")
        site = "https://surf.jackbuehner.com/"
        self.urlbar.setText(site)
        try:
            towrite = f"\n {site}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass        

    def FIREFOXSLITHER(self):
        self.add_new_tab(qurl="https://slither.io")
        site = "https://slither.io"
        self.urlbar.setText(site)     
        try:
            towrite = f"\n {site}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass   
    
    def TRANSLATEPAGE(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urltobe = f"https://translate.google.com/translate?hl=en&sl=auto&tl=en&u={urlfinal}"
        finalsite = QUrl(urltobe)
        print(urltobe)
        print(finalsite)
        self.tabs.currentWidget().setUrl(finalsite)
    
    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):
        old_path = download.url().path()  # download.path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()
                    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))
    
    def screenshot(self):
        try:
            myScreenshot = pyautogui.screenshot()
            root=Tk()
            root.iconify()
            Label(root, text="Temporary Window. Please don't close").pack()
            myScreenshot = pyautogui.screenshot()
            path=fd.asksaveasfilename(
                    defaultextension='.png', filetypes=[("PNG", '*.png')],
                    title="Choose filename")
            myScreenshot.save(path)
            QMessageBox.about(self, "Screenshot Saved", f"The screenshot has been saved in the path {path}")
            root.destroy()
        except:
            pass
    
    def DUPLICATETAB(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        self.add_new_tab(qurl = urlfinal)
    
    def add_new_tab(self, qurl=None, label="New Tab"):

        if qurl is None:
            qurl = QUrl('https://www.google.com/search?q=')
        
        else:
            qurl = QUrl(qurl)
        
        browser = QWebEngineView()
        page = WebEnginePage(browser)
        browser.setPage(page)
        page.printRequested.connect(self.printRequested)
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile(
        ).downloadRequested.connect(self.on_downloadRequested)
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab

        self.tabs.setTabIcon(i, browser.page().icon())

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

        browser.iconChanged.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabIcon(i, browser.icon()))
        q = self.tabs.currentWidget().url()
        justurl = str(q)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]
        try:
            towrite = f"\n {urlfinal}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass
                                     

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        try:
            qurl = self.tabs.currentWidget().url()
            self.update_urlbar( qurl, self.tabs.currentWidget() )
            self.update_title(self.tabs.currentWidget())
        except:
            self.close()
           
    def givealert(self): 
        PRIVATEBROWSER = PrivateWindow()
       
    
    def viewpage(self):
        try:
            qurl = self.tabs.currentWidget().url()
            justurl = str(qurl)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0] 
            viewsource = "view-source:"
            completeurl = f"{viewsource}{urlfinal}"
            self.add_new_tab(qurl = completeurl)
        except IndexError:
            pass
    
    def SHARE_WITH_WHATSAPP(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urlwhatsapp = f"https://web.whatsapp.com/send?text=Link : {urlfinal}"
        webbrowser.open(urlwhatsapp)
    
    def SHARE_WITH_GMAIL(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urlgmail = f"https://mail.google.com/mail/?view=cm&to=&su=Link&body=Link : {urlfinal}"
        webbrowser.open(urlgmail)
    
    def copytext(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        pc.copy(urlfinal)
        QMessageBox.about(self, "Link copied", f"Link has been copied to your clipboard")
    
    def QR_CODE(self):
        import pyqrcode
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        url = pyqrcode.create(urlfinal)
        path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "",
                                                  "SVG (*.svg)")
        url.svg(path, scale=8)
        cwd=os.getcwd() 
        QMessageBox.about(self, "QR Code Saved", f"QR Code has been saved in the path {path}")
        
    def close_current_tab(self, i):
        self.tabs.removeTab(i)
        
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()

        self.setWindowTitle(f"{title} - Dynobite")

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://github.com/abhinavsatheesh/dynfiles/"))
        site = "https://github.com/abhinavsatheesh/dynfiles/"
        self.urlbar.setText(site)
        try:
            towrite = f"\n {site}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass
        
    
    def OPENHISTORY(self):
        try:
            os.startfile(DynobiteHistoryFolder)     
        except:
            with open(DynobiteHistoryFolder, "w") as historyfile:
                historyfile.close()
                os.startfile(DynobiteHistoryFolder) 
            
    
    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
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
            self.urlbar.setText(filename)
        else:
            if filename:
                with open(filename, 'r') as f:
                    html = f.read()

                self.tabs.currentWidget().setHtml(html)
                self.urlbar.setText(filename)
    
    def CLEARHISTORY(self):
        file = open(DynobiteHistoryFolder,"r+")
        file.truncate(0)
        file.close()
        root = Tk()
        root.iconify()
        QMessageBox.about(self, "History Cleared", "History has been cleared")
        root.destroy()
       
    def addnewwindow(self):
        windownew = MainWindow()
    
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):  # Does not receive the Url
        inputtext = self.urlbar.text()
        print(inputtext)
        if validators.url(inputtext):
            q = QUrl(inputtext)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)
        elif validators.url(f"https://{inputtext}"):
            q = QUrl(f"http://{inputtext}")
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)
        elif inputtext.find("file:///") == 0 or inputtext.find("view-source:") == 0 :
            q = QUrl(inputtext)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        else:
            url = f'https://www.google.com/search?q={inputtext.replace("+","%2B").replace(" ","+")}'
            q = QUrl(url)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)
        try:
            towrite = f"\n {urlfinal}"
            with open(DynobiteHistoryFolder, "a+") as historyfile:
                historyfile.write(towrite) 
                historyfile.close()
        except:
            pass
       
        
    def update_urlbar(self, q, browser=None):
        url = q.toString()
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'shield.png')))
            self.httpsicon.setStatusTip("Your connection is secure")

        elif q.scheme() == 'http':
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'signal.png')))
            self.httpsicon.setStatusTip("Your connection is not secure")

        elif q.scheme() == 'file':
                self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'document.png')))
                self.httpsicon.setStatusTip("You are viewing a local or shared file")

        elif q.scheme() == 'view-source':
            # source code padlock icon
            self.httpsicon.setStatusTip(f"You are viewing the source of a website")

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    
class PrivateWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(PrivateWindow, self).__init__(*args, **kwargs)        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab) 
        self.zoom_factor = 2        
        
        self.setCentralWidget(self.tabs)
        
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(32, 32))
        navtb.setMovable(False)
        self.addToolBar(navtb)
        

        back_btn = QAction(QIcon(os.path.join(completedir, 'favicon_back.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join(completedir, 'favicon_forward.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join(completedir, 'favicon_reload.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        stop_btn = QAction(QIcon(os.path.join(completedir, 'favicon_close.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        home_btn = QAction(QIcon(os.path.join(completedir, 'favicon_home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        newtab_btn = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "New Tab", self)
        newtab_btn.setStatusTip("Open a new tab")
        newtab_btn.triggered.connect(lambda _: self.add_new_tab())
        navtb.addAction(newtab_btn)        

        navtb.addSeparator()

        self.httpsicon = QLabel()  
        self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'shield.png')))
        navtb.addWidget(self.httpsicon)     
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setFixedHeight(28)
        navtb.addWidget(self.urlbar)

        navtb.setStyleSheet("""
                                QToolBar {
                                    background-color: #ffffff; 
                                    color:#000000;
                                }
                                QToolBar QToolButton {
                                    background-color: #ffffff;
                                    border-radius: 2px;
                                }
                                QToolBar QToolButton:pressed {
                                    background-color: #AAB0BC;
                                    border-radius: 2px;
                                }
                                
                                """)
        self.tabs.setStyleSheet("""
                                    QTabWidget {
                                        background: #ffffff; 
                                    }
                                    QTabBar {
                                        background: #e7eaed; 
                                    }
                                    QTabBar::tab {
                                        background: #e7eaed; 
                                        padding: 10px;
                                        color: #000000;
                                        margin-top: -1px;
                                        margin-bottom: -1px; 
                                        margin-left: 1pt solid black;
                                        margin-right: 1pt solid black;
                                        border: 1px solid #000000;
                                        border-radius: 4px;
                                    } 
                                    QTabBar::tab:hover { 
                                        background: #f0f0f0;  
                                    } 
                                    QTabBar::tab:selected { 
                                        background: #ffffff;  
                                        color: #000000;
                                    }
                                    """)
        self.urlbar.setStyleSheet(
               "font-size: 10pt;border: 1px solid #0088ff;border-radius: 5px;background-color:#ffffff;color:#000000")
        
        navtb.addSeparator()
        
        btn = QPushButton(':', self)
        btn.resize(32, 32)
        menu = QMenu()
        menu.triggered.connect(lambda x: print(x.text()))
        btn.setMenu(menu)
        btn.setStyleSheet(
               "font-size: 10pt;border: 1px solid #0088ff;border-radius: 5px;background-color:#ffffff;color:#000000")
        
        navtb.addWidget(btn)      
        
        new_tab_action = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        menu.addAction(new_tab_action)
        
        new_window_action = QAction(QIcon(os.path.join(completedir, 'favicon_newwindow.png')), "New Window", self)
        new_window_action.setStatusTip("Open a new window")
        new_window_action.triggered.connect(lambda _: self.addnewwindow())
        menu.addAction(new_window_action)
        
        new_privatewindow_action = QAction(QIcon(os.path.join(completedir, 'favicon_newprivate.png')), "New PrivateBrowse Window", self)
        new_privatewindow_action.setStatusTip("Open a new PrivateBrowse window")
        new_privatewindow_action.triggered.connect(lambda _: self.givealert())
        menu.addAction(new_privatewindow_action)
        
        duplicate_tab_action = QAction(QIcon(os.path.join(completedir, 'favicon_newtabpage.png')), "Duplicate Tab", self)
        duplicate_tab_action.setStatusTip("Duplicate Tab")
        duplicate_tab_action.triggered.connect(self.DUPLICATETAB)
        menu.addAction(duplicate_tab_action)
        
        menu.addSeparator()
        
        open_file_action = QAction(QIcon(os.path.join(completedir, 'favicon_openfile.png')), "Open File", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        menu.addAction(open_file_action)
        
        save_file_action = QAction(QIcon(os.path.join('images', 'favicon_savepage.png')), "Save Page", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        menu.addAction(save_file_action)

        print_file_action = QAction(QIcon(os.path.join('images', 'favicon_savepage.png')), "Print Page", self)
        print_file_action.setStatusTip("Print current page")
        print_file_action.triggered.connect(self.printRequested)
        menu.addAction(print_file_action)
      
        history_action = QAction(QIcon(os.path.join(completedir, 'favicon_history.png')), "History", self)
        history_action.setStatusTip("View Browsing History")
        history_action.triggered.connect(self.OPENHISTORY)
        menu.addAction(history_action)

        clear_history = QAction(QIcon(os.path.join(completedir, 'favicon_history.png')), "Clear History", self)
        clear_history.setStatusTip("Clear Browsing History")
        clear_history.triggered.connect(self.CLEARHISTORY)
        menu.addAction(clear_history)
        
        downloadbutton_action = QAction(QIcon(os.path.join(completedir, 'favicon_downloads.png')), "Downloads", self)
        downloadbutton_action.setStatusTip("Open Downloads Folder")
        downloadbutton_action.triggered.connect(self.OPENDOWNLOADS)
        menu.addAction(downloadbutton_action)
        
        menu.addSeparator()
        
        screenshot_btn = QAction(QIcon(os.path.join(completedir, 'favicon_screenshot.png')), "Screenshot", self)
        screenshot_btn.setStatusTip("Capture Screenshot")
        screenshot_btn.triggered.connect(lambda:self.screenshot())
        menu.addAction(screenshot_btn)
        
        view_source = QAction(QIcon(os.path.join(completedir, 'favicon_pagesource.png')), "View Page Source", self)
        view_source.setStatusTip("View Page Source")
        view_source.triggered.connect(self.viewpage)
        menu.addAction(view_source)
        
        impMenu = QMenu('Share', self)
        
        link_share = QAction(QIcon(os.path.join(completedir, 'favicon_copylink.png')),'Copy Link', self)
        link_share.triggered.connect(self.copytext)
        impMenu.addAction(link_share)
        
        qr_share = QAction(QIcon(os.path.join(completedir, 'favicon_copylink.png')),'Generate QR Code', self)
        qr_share.triggered.connect(self.QR_CODE)
        impMenu.addAction(qr_share)
        
        share_with_whatsapp = QAction(QIcon(os.path.join(completedir, 'favicon_whatsapp.png')),'Share with WhatsApp', self)
        share_with_whatsapp.triggered.connect(self.SHARE_WITH_WHATSAPP)
        impMenu.addAction(share_with_whatsapp)
        
        share_with_gmail = QAction(QIcon(os.path.join(completedir, 'favicon_gmail.png')),'Share with Gmail', self)
        share_with_gmail.triggered.connect(self.SHARE_WITH_GMAIL)
        impMenu.addAction(share_with_gmail)

        menu.addMenu(impMenu)
       
        translate_action = QAction(QIcon(os.path.join(completedir, 'favicon_translate.png')), "Translate Page", self)
        translate_action.setStatusTip("Translate the current page")
        translate_action.triggered.connect(self.TRANSLATEPAGE)
        menu.addAction(translate_action)
        
        menu.addSeparator()

        game_surf_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Surf", self)        
        game_surf_action.setStatusTip("Play Surf")
        game_surf_action.triggered.connect(self.EDGESURF)
        menu.addAction(game_surf_action)

        game_dino_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Dino", self)        
        game_dino_action.setStatusTip("Play Dino")
        game_dino_action.triggered.connect(self.CHROMEDINO)
        menu.addAction(game_dino_action)   

        game_slitheraction = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Slither", self)        
        game_slitheraction.setStatusTip("Play Slither")
        game_slitheraction.triggered.connect(self.FIREFOXSLITHER)
        menu.addAction(game_slitheraction)
        
        game_shell_action = QAction(QIcon(os.path.join(completedir, 'games.png')), "Play Shell Shocker", self)        
        game_shell_action.setStatusTip("Play Shell Shocker")
        game_shell_action.triggered.connect(self.SHELLSHOCK)
        menu.addAction(game_shell_action)
        
        menu.addSeparator()
        
        about_action = QAction(QIcon(os.path.join(completedir, 'question.png')), "About Dynobite", self)
        about_action.setStatusTip("Find out more about Dynobite")
        about_action.triggered.connect(self.about)
        menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join(completedir, 'favicon_home.png')),
                                            "Dynobite Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Dynobite Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        menu.addAction(navigate_mozarella_action)
        
        URL = "https://www.google.co.in"
        self.add_new_tab(QUrl(URL), 'Homepage')
        self.NewTabListener = QShortcut(QKeySequence('Ctrl+T'), self)
        self.NewTabListener.activated.connect(lambda : self.add_new_tab())
        self.NewWindowListener = QShortcut(QKeySequence('Ctrl+N'), self)
        self.NewWindowListener.activated.connect(lambda : self.addnewwindow())
        self.PrivateWindowListener = QShortcut(QKeySequence('Ctrl+Shift+N'), self)
        self.PrivateWindowListener.activated.connect(lambda : self.givealert())
        self.HistoryListener = QShortcut(QKeySequence('Ctrl+H'), self)
        self.HistoryListener.activated.connect(lambda : self.OPENHISTORY())
        self.ClearHistoryListener = QShortcut(QKeySequence('Ctrl+Shift+Del'), self)
        self.ClearHistoryListener.activated.connect(lambda : self.CLEARHISTORY())
        self.DuplicateTabListener = QShortcut(QKeySequence('Ctrl+K'), self)
        self.DuplicateTabListener.activated.connect(lambda : self.DUPLICATETAB())
        self.OpenFileListener = QShortcut(QKeySequence('Ctrl+O'), self)
        self.OpenFileListener.activated.connect(lambda : self.open_file())
        self.SaveFileListener = QShortcut(QKeySequence('Ctrl+S'), self)
        self.SaveFileListener.activated.connect(lambda : self.save_file())
        self.ScreenshotListener = QShortcut(QKeySequence('Ctrl+Shift+S'), self)
        self.ScreenshotListener.activated.connect(lambda : self.screenshot())
        self.ViewSourceListener = QShortcut(QKeySequence('Ctrl+U'), self)
        self.ViewSourceListener.activated.connect(lambda : self.viewpage())
        self.DownloadListener = QShortcut(QKeySequence('Ctrl+J'), self)
        self.DownloadListener.activated.connect(lambda : self.OPENDOWNLOADS())
        self.ReloadListener = QShortcut(QKeySequence("Ctrl+R"), self)
        self.ReloadListener.activated.connect(lambda : self.tabs.currentWidget().reload())
        self.ReloadListener1 = QShortcut(QKeySequence("F5"), self)
        self.ReloadListener1.activated.connect(lambda : self.tabs.currentWidget().reload())

        self.menuBar().setNativeMenuBar(False)
        self.show()
        self.setWindowTitle("Dynobite")
        self.setWindowIcon(QIcon(os.path.join(completedir, '1.png')))
            
    def closeEvent(self, event):
        if self.tabs.count() > 1:
            reply = QMessageBox.question(self, 'Close all tabs?', f'You have {self.tabs.count()} tabs open', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()      
        else:
            self.close()
   
    def OPENDOWNLOADS(self):
        os.startfile(completedownloaddir)
        
    def printRequested(self):
            # if you are viewing this part of my code can you please improve this as I don't think this is the best way to print a page and I can't understand how to fix this
            url = self.urlbar.text()
            if url == "":
                url = 'file:///html/home.html'
            self.view = QtWebEngineWidgets.QWebEngineView()
            self.page = QtWebEngineWidgets.QWebEnginePage(self)
            self.view.setPage(self.page)
            self.view.load(QtCore.QUrl(url))
            defaultPrinter = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinterInfo.defaultPrinter())
            dialog = QtPrintSupport.QPrintDialog(defaultPrinter, self)
            if dialog.exec():
                # printer object has to be persistent
                self._printer = dialog.printer()
                self.page.print(self._printer, self.printResult)

    def printResult(self, success):
        if success:
            pass
        else:
            QtWidgets.QMessageBox.information(self, 'Print failed',
                                                 'Printing has failed!', QtWidgets.QMessageBox.Ok)
        del self._printer
      
    def SHELLSHOCK(self):
        self.add_new_tab(qurl="https://shellshock.io/")
        site = "https://shellshock.io/"
        self.urlbar.setText(site)

    def EDGESURF(self):
        self.add_new_tab(qurl="https://surf.jackbuehner.com/")
        site = "https://surf.jackbuehner.com/"
        self.urlbar.setText(site)

    def CHROMEDINO(self):
        self.add_new_tab(qurl="http://wayou.github.io/t-rex-runner/")
        site = "https://surf.jackbuehner.com/"
        self.urlbar.setText(site)
      

    def FIREFOXSLITHER(self):
        self.add_new_tab(qurl="https://slither.io")
        site = "https://slither.io"
        self.urlbar.setText(site)     
    
    def TRANSLATEPAGE(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urltobe = f"https://translate.google.com/translate?hl=en&sl=auto&tl=en&u={urlfinal}"
        finalsite = QUrl(urltobe)
        print(urltobe)
        print(finalsite)
        self.tabs.currentWidget().setUrl(finalsite)
    
    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):
        old_path = download.url().path()  # download.path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()
                    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))
    
    def screenshot(self):
        try:
            myScreenshot = pyautogui.screenshot()
            root=Tk()
            root.iconify()
            Label(root, text="Temporary Window. Please don't close").pack()
            myScreenshot = pyautogui.screenshot()
            path=fd.asksaveasfilename(
                    defaultextension='.png', filetypes=[("PNG", '*.png')],
                    title="Choose filename")
            myScreenshot.save(path)
            QMessageBox.about(self, "Screenshot Saved", f"The screenshot has been saved in the path {path}")
            root.destroy()
        except:
            pass
    
    def DUPLICATETAB(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        self.add_new_tab(qurl = urlfinal)
    
    def add_new_tab(self, qurl=None, label="New Tab"):

        if qurl is None:
            qurl = QUrl('https://www.google.com/search?q=')
        
        else:
            qurl = QUrl(qurl)
        
        browser = QWebEngineView()
        page = WebEnginePage(browser)
        browser.setPage(page)
        page.printRequested.connect(self.printRequested)
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile(
        ).downloadRequested.connect(self.on_downloadRequested)
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab

        self.tabs.setTabIcon(i, browser.page().icon())

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

        browser.iconChanged.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabIcon(i, browser.icon()))
                                    

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        try:
            qurl = self.tabs.currentWidget().url()
            self.update_urlbar( qurl, self.tabs.currentWidget() )
            self.update_title(self.tabs.currentWidget())
        except:
            self.close()
           
    def givealert(self): 
        PRIVATEBROWSER = PrivateWindow()
       
    
    def viewpage(self):
        try:
            qurl = self.tabs.currentWidget().url()
            justurl = str(qurl)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0] 
            viewsource = "view-source:"
            completeurl = f"{viewsource}{urlfinal}"
            self.add_new_tab(qurl = completeurl)
        except IndexError:
            pass
    
    def SHARE_WITH_WHATSAPP(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urlwhatsapp = f"https://web.whatsapp.com/send?text=Link : {urlfinal}"
        webbrowser.open(urlwhatsapp)
    
    def SHARE_WITH_GMAIL(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        urlgmail = f"https://mail.google.com/mail/?view=cm&to=&su=Link&body=Link : {urlfinal}"
        webbrowser.open(urlgmail)
    
    def copytext(self):
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        pc.copy(urlfinal)
        QMessageBox.about(self, "Link copied", f"Link has been copied to your clipboard")
    
    def QR_CODE(self):
        import pyqrcode
        qurl = self.tabs.currentWidget().url()
        justurl = str(qurl)
        firsttime = justurl.split("PyQt5.QtCore.QUrl('")
        urlneeded = firsttime[1]
        justurl = str(urlneeded)
        secondtime = justurl.split("')")
        urlfinal = secondtime[0]   
        url = pyqrcode.create(urlfinal)
        path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "",
                                                  "SVG (*.svg)")
        url.svg(path, scale=8)
        cwd=os.getcwd() 
        QMessageBox.about(self, "QR Code Saved", f"QR Code has been saved in the path {path}")
        
    def close_current_tab(self, i):
        self.tabs.removeTab(i)
        
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()

        self.setWindowTitle(f"{title} - Dynobite")

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://github.com/abhinavsatheesh/dynfiles/"))
        site = "https://github.com/abhinavsatheesh/dynfiles/"
        self.urlbar.setText(site)
        
    
    def OPENHISTORY(self):
        try:
            os.startfile(DynobiteHistoryFolder)     
        except:
            with open(DynobiteHistoryFolder, "w") as historyfile:
                historyfile.close()
                os.startfile(DynobiteHistoryFolder) 
            
    
    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
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
            self.urlbar.setText(filename)
        else:
            if filename:
                with open(filename, 'r') as f:
                    html = f.read()

                self.tabs.currentWidget().setHtml(html)
                self.urlbar.setText(filename)
    
    def CLEARHISTORY(self):
        file = open(DynobiteHistoryFolder,"r+")
        file.truncate(0)
        file.close()
        root = Tk()
        root.iconify()
        QMessageBox.about(self, "History Cleared", "History has been cleared")
        root.destroy()
       
    def addnewwindow(self):
        windownew = MainWindow()
    
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):  # Does not receive the Url
        inputtext = self.urlbar.text()
        print(inputtext)
        if validators.url(inputtext):
            q = QUrl(inputtext)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)
        elif validators.url(f"https://{inputtext}"):
            q = QUrl(f"http://{inputtext}")
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)
        elif inputtext.find("file:///") == 0 or inputtext.find("view-source:") == 0 :
            q = QUrl(inputtext)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        else:
            url = f'https://www.google.com/search?q={inputtext.replace("+","%2B").replace(" ","+")}'
            q = QUrl(url)
            justurl = str(q)
            firsttime = justurl.split("PyQt5.QtCore.QUrl('")
            urlneeded = firsttime[1]
            justurl = str(urlneeded)
            secondtime = justurl.split("')")
            urlfinal = secondtime[0]
            print(urlfinal)

        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)
       
        
    def update_urlbar(self, q, browser=None):
        url = q.toString()
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'shield.png')))
            self.httpsicon.setStatusTip("Your connection is secure")

        elif q.scheme() == 'http':
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'signal.png')))
            self.httpsicon.setStatusTip("Your connection is not secure")

        elif q.scheme() == 'file':
                self.httpsicon.setPixmap(QPixmap(os.path.join(completedir, 'document.png')))
                self.httpsicon.setStatusTip("You are viewing a local or shared file")

        elif q.scheme() == 'view-source':
            # source code padlock icon
            self.httpsicon.setStatusTip(f"You are viewing the source of a website")

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
app.setApplicationName("Dynobite")
app.setOrganizationName("Dyn")
window = MainWindow()

app.exec_()
