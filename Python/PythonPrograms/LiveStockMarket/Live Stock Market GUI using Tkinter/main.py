from tkinter import *
from tkinter import font
from yahoo_fin import stock_info
from share_list import l_sharelist
import os, webbrowser, threading, sqlite3

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Wealthfolio")
        self.state("zoomed")
        conn = sqlite3.connect('database.db')
        self.cursor = conn.cursor()
        create_table_query = '''SELECT * FROM my_stocks;'''
        try:
            self.cursor.execute(create_table_query)
        except:
            for i in range(0, 10, 1):
                spacer_label = Label(self, text="")
                spacer_label.pack()
            bold_font = font.Font(weight="bold", size=15)
            no_stocks_found = Label(self, text="No stocks added", font=bold_font)
            no_stocks_found.pack()
            add_stocks_
App = MainWindow()
App.mainloop()
