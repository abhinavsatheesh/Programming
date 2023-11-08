from tkinter import *
from tkinter import messagebox
import os
import platform
from tkinter import ttk	
import wmi
import os
import cpuinfo
import threading
import psutil as p

currentpath = os.getcwd()
folderto = "Dynomo Files"
imagesfolder = "Images"
completepath = os.path.join(currentpath, folderto)
completeimagepath = os.path.join(folderto, imagesfolder)
lightdardir = os.path.join(completepath, "LightDarkMode.txt")
wallpapercolor = os.path.join(completepath, "WallpaperColor.txt")
oobedone = os.path.join(completepath, "OOBEDone.txt")
wallpaperimage = os.path.join(completepath, "WallpaperImage.txt")
nameuser = os.path.join(completepath, "BasicConfig.txt")
passworddir = os.path.join(completepath, "PasswordChecker.txt")  


try:
    os.mkdir(completepath) 
    os.mkdir(completeimagepath)
    with open(lightdardir, "w") as file1:
        if file1=="":
            file1.write("Dark Mode")
            file1.close()            
        elif file1=="Light Mode":
            pass
            file1.close()
        elif file1=="Dark Mode":
            file1.close()
        else:
            file1.write("Dark Mode")
            file1.close()

    with open(wallpapercolor, "w") as file1:
        if file1=="":
            file1.write("#2CD5FF")
            file1.close()            
        else:
            file1.close()
    with open(wallpaperimage, "w") as file1:
        if file1=="":
            file1.close()
        elif file1=="Wallpaper Selected":
            file1.close()
        else:
            file1.close()

except FileExistsError:
    pass

if os.path.isfile(passworddir) == True:
    pass

else:
    with open(passworddir, "w+") as file1:
        pass

if os.path.isfile(oobedone) == True:
    pass

else:
    with open(oobedone, "w+") as file1:
        pass

if os.path.isfile(nameuser) == True:
    pass

else:
    with open(nameuser, "w+") as file1:
        pass

if os.path.isfile(oobedone) == True:
	pass

else:
	with open(oobedone, "w+") as file1:
		pass

with open(wallpapercolor, "r+") as file1:
    colorofscreen = file1.read()
    if colorofscreen == "":
        colorofscreen = "#2CD5FF"

with open(lightdardir, "r+") as file2:
    lightordark = file2.read()
    if lightordark == "Dark Mode":
        bg1 = "black"
        fg1 = "white"
    else:
        bg1 = "white"
        fg1 = "black"

c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]

def size(byte):
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

class BackgroundTasks(threading.Thread):
    def run(self):
        mem = p.virtual_memory()
        totalram = size(mem.total)  
        cpuname = cpuinfo.get_cpu_info()['brand_raw'] 
        uname = platform.uname()
        self.systemdetails = f"Base OS : {uname.system}\nMachine Name : {uname.node}\nVersion : {uname.version}\nMachine : {uname.machine}\nProcessor : {cpuname}\nTotal Memory : {totalram}\nManufacturer : {my_system.Manufacturer}\nModel : {my_system. Model}\nSystem Type : {my_system.SystemType}"

BackgroundStart = BackgroundTasks()
BackgroundStart.start()

class PasswordSet(Tk):
	def __init__(self):
		super().__init__()
		self.PASSWORDENTERED = StringVar(self)
		self.configure(bg="white")
		self.title("Set a new Password")
		self.protocol("WM_DELETE_WINDOW", self.goback1)
		self.label1 = Label(self, text="Set a new password", bg="white").pack()
		self.entry1 = Entry(self, textvariable = self.PASSWORDENTERED, show="*").pack()
		self.label2 = Label(self, text="", bg="white").pack()
		self.button1 = Button(self, text="Set password", command=self.setpassword).pack()
		self.mainloop()

	def setpassword(self):
		self.passwordinput = self.PASSWORDENTERED.get()
		mylist = list(self.passwordinput)
		res = [x + ('1234dyn' if i else '') for i, x in enumerate(mylist)]
		res[0] = res[0] + '1234dyn'
		def listToString(s): 
			str1 = "" 
			for ele in s: 
				str1 += ele  
			return str1 
		self.completestring = (listToString(res))
		with open(passworddir, "w+") as file1:
			file1.write(self.completestring)
		messagebox.showinfo("Name and Password Updated", "Your name and password has been set successfully")
		self.destroy()
		Proceed = OutOfTheBoxExperience3()

	def goback1(self):
		self.destroy()
		go = OutOfTheBoxExperience2()

class OutOfTheBoxExperience1(Tk):
	def __init__(self):
		super().__init__()
		self.title("Welcome to Dynomo")
		self.configure(bg="white")
		self.state("zoomed")
		# self.frames = PhotoImage(file='Dynomo Files\Images\hello_PNG12.png')
		# self.hello = Label(self, image=self.frames, height=500, width=500, bg="white").place(x=400, y=0)
		# self.label = Label(self, image=self.frames)
		self.proceedbutton = Button(self, text="➡", command = self.proceedtonameusernamepassword, font=("Calibri", "20")).place(x=620, y=400)
		self.mainloop()

	def proceedtonameusernamepassword(self):
		self.destroy()
		Proceed = OutOfTheBoxExperience2()

class OutOfTheBoxExperience2(Tk):
	def __init__(self):
		super().__init__()
		self.title("Name, Username and Password")
		self.state("zoomed")
		# self.basicphoto = PhotoImage(file = "Dynomo Files\Images\BasicDetails.png", master=self)
		# self.basicdetails = Label(self, image=self.basicphoto).place(x=800, y=100)
		self.clicked = StringVar(self)
		self.nameofuser = StringVar(self)
		self.emailofuser = StringVar(self)
		self.clicked.set("Authentication Mode")
		options = ["Password Protection (Recommended)", "No Protection (Not Secure)"]
		self.heading = Label(self, text="Enter your basic details", font=("Calibri", "20")).place(x=550, y=0)
		self.entername = Label(self, text="Enter your name", font=("Calibri", "20")).place(x=0, y=100)
		self.nameuser = Entry(self, textvariable = self.nameofuser, font=("Calibri", "20")).place(x=300, y=100)
		self.entermailid = Label(self, text="Enter your mail ID", font=("Calibri", "20")).place(x=0, y=200)
		self.mailuser = Entry(self, textvariable = self.emailofuser, font=("Calibri", "20")).place(x=300, y=200)

		options = [
			"Password Protection",
			"No Protection"
		]

		self.clicked.set("Authentication Mode")
		self.drop = OptionMenu(self, self.clicked , *options )
		self.drop.place(x=400, y=300)
		self.enterpassword = Label(self, text="Select your Authentication Mode", font=("Calibri", "20")).place(x=0, y=300)
		self.gobackbutton = Button(self, text="⬅", command = self.goback, font=("Calibri", "20")).place(x=520, y=400)
		self.proceedbutton = Button(self, text="➡", command = self.check, font=("Calibri", "20")).place(x=620, y=400)

	
	def goback(self):
		self.destroy()
		DoOOBE = OutOfTheBoxExperience1()

	def check(self):
		nameofuser = self.nameofuser.get()
		mailofuser = self.emailofuser.get()
		with open(nameuser, "w+") as file1:
			file1.write(f"{nameofuser}\n{mailofuser}")
		userinput = self.clicked.get()
		if userinput == "Authentication Mode":
			pass
		elif userinput == "Password Protection":
			result = messagebox.askquestion("Confirm Details", f"You have entered your name as {nameofuser}.\nYou have also chosen a Password as authentication. Proceed to Password Setup?")
			if result == "yes":
				self.destroy()
				NewPassword = PasswordSet()			
			else:
				pass
		else:
			result = messagebox.askquestion("Confirm Details", f"You have entered your name as {nameofuser}.\nYou have chosen to move without a password. Dynomo recommends that you keep a password so that your device is not vulnerable to any attacks. Proceed without a Password?")	
			if result == "yes":
				self.destroy()
				Proceed = OutOfTheBoxExperience3()
			else:
				pass

class OutOfTheBoxExperience3(Tk):
	def __init__(self):
		super().__init__()
		self.title("Computer Details")
		self.state("zoomed")
		# self.computerphoto = PhotoImage(file = "Dynomo Files\Images\ComputerIcon.png", master=self)
		# self.basicdetails = Label(self, image=self.computerphoto).place(x=800, y=100)
		self.heading = Label(self, text="Are these details regarding your Computer correct?", font=("Calibri", "20")).pack()
		self.explanation = Label(self, text="These details will help us optimise Dynomo for your PC", font=("Calibri", "20")).pack()
		self.computerdetails = Label(self, text=BackgroundStart.systemdetails, font=("Calibri", "20")).place(x=50, y=100)
		self.gobackbutton = Button(self, text="⬅", font=("Calibri", "20"), command=self.goback).place(x=520, y=500)
		self.proceedbutton = Button(self, text="➡", font=("Calibri", "20"), command=self.check).place(x=620, y=500)

	def goback(self):
		self.destroy()
		GoBack = OutOfTheBoxExperience2()

	def check(self):
		self.destroy()
		LastStep = OutOfTheBoxExperience4()

class OutOfTheBoxExperience4(Tk):
	def __init__(self):
		super().__init__()
		self.title("Done!")
		self.state("zoomed")
		self.mainLabel = Label(self, text="Done!\nThe Out of the Box Experience (OOBE) is done. Dynomo is ready to run now, optimised for you and your PC\nDynomo is, and will always remain free of cost, speedy, and customised", font=("Calibri", "20")).pack()
		self.spacing = Label(self, text="").pack()
		self.spacing = Label(self, text="").pack()
		self.explnanationlabel = Label(self, text="Dynomo consists of many power-packed apps\n which helps you to get up and running in a very quick time. The apps include Dynobite (Browser),\n Dynofite (Word Processor), Dynapite (App Development Tool), Dynotite (Terminal),\n a Voice Recorder, a Camera, and of course a Calculator", font=("Calibri", "20")).pack()
		self.spacing = Label(self, text="").pack()
		self.start = Button(self, text="Start your Dynomo journey now!", command=self.STARTDYNOMO).pack()
		self.mainloop()

	def STARTDYNOMO(self):
		with open(oobedone, "w+") as file3:
			file3.write("OOBE Done")
		self.destroy()
		os.system("python Dynomo.py")

DoOOBE = OutOfTheBoxExperience1()
DoOOBE.mainloop()