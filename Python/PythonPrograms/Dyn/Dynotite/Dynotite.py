from tkinter import *
from tkinter import filedialog as fd 
import os
from sys import platform
import threading
import time

#Version = Version 6

def debug(data):
    print (data)

def save():
    code=CODE.get("1.0",'end-1c')
    name=NAMETEXT.get()
    filename1 = fd.askdirectory()
    finaldir=f"{filename1}/{name}.py"
    with open(finaldir, 'w') as f:
        f.write(code)

def OPENYOURFILE():
    filename2 = fd.askopenfilename(
                filetypes=(
                    ("Python Files", "*.py"),
                )
            )
    nameofappentry = entryname.get()
    os.system(f"python -m PyInstaller --onefile --name {nameofappentry} --noconsole {filename2}")

def EXECUTE():
    subject = CODE.get("1.0",'end-1c')
    exec(subject)
    print ("---------------------------------------------")

def INSTALLPIP():
    install = pip.get("1.0",'end-1c')
    package=f"pip install {install}"
    os.system(package)

TERMNAL=Tk()
TERMNAL.title("Dynotite - The Terminal Faster Than Python Itself")
TERMNAL.geometry('750x1500')
TERMNAL.state('zoomed')
TERMNAL.configure(bg='#40358A')
PYTHONCODE=Label(TERMNAL, text="Type your Python Code Below 👇", bg='#40358A', fg='white')
PYTHONCODE.place(x=10, y=10)
CODE = Text(TERMNAL)
CODE.place(x=10, y=40,width=700,height=300)
GETEXEC=Button(TERMNAL, text="Execute",command=EXECUTE)
GETEXEC.place(x=300, y=350)
NAME=Label(TERMNAL, text="Name of File", bg='#40358A', fg='white').place(x=10, y=400)
NAMETEXT=Entry(TERMNAL)
NAMETEXT.place(x=260, y=400)
ppyy=Label(TERMNAL, text=".py", bg='#40358A', fg='white').place(x=390, y=400)
SAVE=Button(TERMNAL, text="Save", command=save)
SAVE.place(x=308, y=460)

INSTALLLABEL=Label(TERMNAL, text="Install PyPi Packages via Pip Below 👇. Just type the Package Name", bg='#40358A', fg='white')
INSTALLLABEL.place(x=800, y=10)
pip = Text(TERMNAL)
pip.place(x=800, y=40, width=400, height=20)
GETPIP=Button(TERMNAL, text="Install", command=INSTALLPIP)
GETPIP.place(x=970, y=70)

if platform == "linux" or platform == "linux2":
    PACKAGINNOTSUPPORTEYET = Label(TERMNAL, text="Packaging Apps for Linux not yet supported in Dynotite", bg='#40358A', fg='white')
    PACKAGINNOTSUPPORTEYET.place(x=800, y=150)
elif platform == "darwin":
    PACKAGINNOTSUPPORTEYET = Label(TERMNAL, text="Packaging Apps for MacOS not yet supported in Dynotite", bg='#40358A', fg='white')
    PACKAGINNOTSUPPORTEYET.place(x=800, y=150)
elif platform == "win32":
    PACKAGINSUPPORTEYET = Label(TERMNAL, text="Package your Apps for Windows 👇.", bg='#40358A', fg='white')
    PACKAGINSUPPORTEYET.place(x=800, y=120)
    nameofapp = Label(TERMNAL, text="Enter the Name of the App. No Spaces Allowed", bg='#40358A', fg='white')
    nameofapp.place(x=800, y=160)
    entryname = Entry(TERMNAL)
    entryname.place(x=940, y=200)    
    PACKAGE = Button(TERMNAL, text="Open and Package App", command=OPENYOURFILE)
    PACKAGE.place(x=940, y=240)
    
print("Dynotite\nVersion 6")
TERMNAL.mainloop()