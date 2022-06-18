from tkinter import *
import os
import urllib.request
import json
import wmi
import os
import threading
import cpuinfo
import psutil as p
import platform
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

def size(byte):
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

class BackgroundTasks(threading.Thread):
    def run(self):
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
            self.countryname = data["country_name"]
        mem = p.virtual_memory()
        totalram = size(mem.total)  
        cpuname = cpuinfo.get_cpu_info()['brand_raw'] 
        uname = platform.uname()
        self.systemdetails = f"Base OS : {uname.system}\nMachine Name : {uname.node}\nVersion : {uname.version}\nMachine : {uname.machine}\nProcessor : {cpuname}\nTotal Memory : {totalram}\nManufacturer : {my_system.Manufacturer}\nModel : {my_system. Model}\nSystem Type : {my_system.SystemType}"
        anvil.server.connect("QSRNKBI6K4U5TLM4BPGOFZWI-637VXAB2QGVW2F64")
        self.dynomorow = app_tables.dynomocurrentversion.get(CurrentVersionDetails="Dynomo Version")
        self.currentdynomoserver = str(self.dynomorow['CurrentVersion'])

        
currentpath = os.getcwd()
folderto = "Dynomo Files"
imagesfolder = "Images"
completepath = os.path.join(currentpath, folderto)
completeimagepath = os.path.join(folderto, imagesfolder)
lightdardir = os.path.join(completepath, "LightDarkMode.txt")
wallpapercolor = os.path.join(completepath, "WallpaperColor.txt")
wallpaperimage = os.path.join(completepath, "WallpaperImage.txt")
nameuser = os.path.join(completepath, "BasicConfig.txt")
passworddir = os.path.join(completepath, "PasswordChecker.txt")  
oobedone = os.path.join(completepath, "OOBEDone.txt")

with open(nameuser, "r+") as file1:
    nameofuser = file1.read()

class Settings(Tk):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self.state("zoomed")
        self.configure(bg="#FFE5B4")
        self.namelabel = Label(self, text=nameofuser, bg="#FFE5B4").place(x=30, y=10)
        self.system = Button(self, text="System", width=33).place(x=0, y=70)
        self.network = Button(self, text="Network", width=33).place(x=0, y=120)
        self.personalisation = Button(self, text="Personalisation", width=33).place(x=0, y=170)
        self.accounts = Button(self, text="Accounts", width=33).place(x=0, y=220)
        self.time = Button(self, text="Time & Region", width=33).place(x=0, y=270)
        self.developerbutton = Button(self, text="Developer Settings", width=33).place(x=0, y=320)
        self.updatebutton = Button(self, text="Dynomo Updater", width=33, command=self.updateframe).place(x=0, y=370)
        self.frame1 = Frame(self)
        self.frame1.place(x=500, y=500)
        self.BackgroundStart = BackgroundTasks()
        self.BackgroundStart.start()
        
    def updateframe(self):
        self.frame1.destroy()
        self.frame1 = Frame(self, bg="#FFE5B4")
        self.label1 = Label(self.frame1, text="Dynomo Updater", bg="#FFE5B4", font=("Calibri", "20")).pack()
        self.spacer = Label(self.frame1, text="", bg="#FFE5B4").pack()
        self.label2 = Label(self.frame1, text="Current Dynomo Version : Version 9", bg="#FFE5B4", font=("Calibri", "20")).pack()
        self.button2 = Button(self.frame1, text="What's new in this update", bg="#3700B4", fg="white").pack()
        self.spacer = Label(self.frame1, text="", bg="#FFE5B4").pack()
        self.button1 = Button(self.frame1, text="Check for Updates", bg="#3700B4", fg="white", command=self.checkupdates).pack()
        self.label3 = Label(self.frame1, text="", bg="#FFE5B4")
        self.label3.pack()
        self.frame1.pack()  

    def checkupdates(self):
        try:
            if self.BackgroundStart.currentdynomoserver == "9":
                self.label3.config(text="Latest updates installed.")
            else:
                self.label3.config(text=f"Updates available to Dynomo {self.BackgroundStart.currentdynomoserver}")
        except:
            pass

SettingsApp = Settings()
SettingsApp.mainloop()
