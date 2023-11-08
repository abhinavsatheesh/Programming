from tkinter import *
from math import sqrt

try:
    class Calculator(Tk):
        def __init__(self):
            super().__init__()
            self.title("Calculator")
            self.geometry("290x500")
            # self.iconphoto(False, PhotoImage(file='favicon.png'))
            self.mystring = StringVar(self)
            self.calculations = Entry(self, textvariable = self.mystring, font = "Helvetica 20 bold")
            self.calculations.place(width=287,height=50)
            self.buttonpercentage = Button(self, text="%", width=8, height=3, command=lambda: self.addnumbertoentry("%")).place(x=0, y=50)
            self.button9 = Button(self, text="C", width=18, height=3, command=self.cleartext).place(x=72, y=50)
            self.buttonx = Button(self, text="⌫", width=8, height=3, command=self.clearlasttext).place(x=213, y=50)
            self.buttondividex = Button(self, text="1/x", width=8, height=3, command=self.addoneby).place(x=0, y=115)
            self.buttonraisedto = Button(self, text="x\u00b2", width=8, height=3, command=self.addexponents).place(x=71, y=115)
            self.buttonrootx = Button(self, text="√x", width=8, height=3, command=self.squareroot).place(x=142, y=115)
            self.buttondivide = Button(self, text="÷", width=8, height=3, command=lambda: self.addnumbertoentry("/")).place(x=213, y=115)
            self.button7 = Button(self, text="7", width=8, height=3, command=lambda: self.addnumbertoentry("7")).place(x=0, y=180)
            self.button8 = Button(self, text="8", width=8, height=3, command=lambda: self.addnumbertoentry("8")).place(x=71, y=180)
            self.button9 = Button(self, text="9", width=8, height=3, command=lambda: self.addnumbertoentry("9")).place(x=142, y=180)
            self.buttonx = Button(self, text="X", width=8, height=3, command=lambda: self.addnumbertoentry("*")).place(x=213, y=180)
            self.button4 = Button(self, text="4", width=8, height=3, command=lambda: self.addnumbertoentry("4")).place(x=0, y=245)
            self.button5 = Button(self, text="5", width=8, height=3, command=lambda: self.addnumbertoentry("5")).place(x=71, y=245)
            self.button6 = Button(self, text="6", width=8, height=3, command=lambda: self.addnumbertoentry("6")).place(x=142, y=245)
            self.buttonminus = Button(self, text="-", width=8, height=3, command=lambda: self.addnumbertoentry("-")).place(x=213, y=245)
            self.button1 = Button(self, text="1", width=8, height=3, command=lambda: self.addnumbertoentry("1")).place(x=0, y=310)
            self.button2 = Button(self, text="2", width=8, height=3, command=lambda: self.addnumbertoentry("2")).place(x=71, y=310)
            self.button3 = Button(self, text="3", width=8, height=3, command=lambda: self.addnumbertoentry("3")).place(x=142, y=310)
            self.buttonplus = Button(self, text="+", width=8, height=3, command=lambda: self.addnumbertoentry("+")).place(x=213, y=310)
            self.buttonplusminus = Button(self, text="+/-", width=8, height=3).place(x=0, y=375)
            self.button2 = Button(self, text="0", width=8, height=3, command=lambda: self.addnumbertoentry("0")).place(x=71, y=375)
            self.button3 = Button(self, text=".", width=8, height=3, command=lambda: self.addnumbertoentry(".")).place(x=142, y=375)
            self.buttonplus = Button(self, text="=", width=8, height=3, bg="#3D78EF", command=self.equaltopressed).place(x=213, y=375)
            menubar = Menu(self)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Keep Window on Top", command=self.keepwindow)
            menubar.add_cascade(label="File", menu=filemenu)
            self.config(menu = menubar)
        
        def squareroot(self):
            self.tobe = self.mystring.get()
            try:
                self.tocalc = int(self.tobe)
            except:
                pass
            self.complete = str(eval(f"sqrt({self.tocalc})"))
            self.tobecompleted = list(self.complete)
            self.tobecompleted.pop()
            self.dot = "."
            for self.dot in self.tobecompleted:
                if self.dot == self.tobecompleted[-1]:
                    self.tobecompleted.pop()
                else:
                    pass
                if " " in self.tobecompleted:
                    self.tobecompleted.remove(" ")
                else:
                    pass
            self.mystring.set(self.tobecompleted)

        def addexponents(self):
            self.tobe = self.mystring.get()
            self.tocalc = self.tobe + "**2"
            try:
                self.complete = eval(self.tocalc)
            except:
                self.tobe = str(self.mystring.get())
                self.tobe1 = str(self.tobe[2])
                self.tocalc = self.tobe1 + "**2"
                self.complete = eval(self.tocalc)
            self.mystring.set(self.complete)

        def addoneby(self):
            self.calculations.insert(INSERT, "1/")

        def clearlasttext(self):
            try:
                self.tobe = self.mystring.get()
                self.length = list(self.tobe)
                self.length.pop()
                a = ""
                for l in self.length:
                    a = a+l
                self.mystring.set(a)
            except:
                pass

        def cleartext(self):
            self.mystring.set("")

        def equaltopressed(self):
            try:
                self.tobe = self.mystring.get()
                if self.tobe == "":
                    pass
                else:
                    self.calculation = eval(self.tobe)
                    self.mystring.set(self.calculation)
            except Exception as e:
                self.mystring.set("Calculation Error")

        def addnumbertoentry(self, number):
            self.TextCurrent = self.mystring.get()
            self.TextCurrent = self.TextCurrent + number
            self.mystring.set(self.TextCurrent)

        def keepwindow(self):
            self.state = self.attributes('-topmost')
            if self.state == 1:
                self.attributes('-topmost', False)
            elif self.state == 0:
                self.attributes('-topmost', True)
            else:
                self.attributes('-topmost', True)
except:
    pass

CalculatorMethod = Calculator()
CalculatorMethod.mainloop()

