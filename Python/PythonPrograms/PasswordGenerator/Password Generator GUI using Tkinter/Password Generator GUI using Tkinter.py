import string
import random
import sys
from tkinter import *
import pyperclip

def helloCallBack():
   pyperclip.copy(passwords)

adject = ['enormous', 'doglike', 'silly', 'yellow', 'fun', 'fast', 'beautiful', 'sleepy', 'slow', 'smelly','wet', 'fat', 'red','orange', 'yellow', 'green', 
'blue', 'purple', 'fluffy','white', 'proud', 'brave', 'adorable', 'amused', 'annoying', 'ashamed', 'awful', 'better', 'bloody', 'blushing', 'brave', 'busy']

nou = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda', 'more', 'some ', 'telephone', 'banana', 'teacher']

ad=random.choice(adject)
no=random.choice(nou)
number=str(random.randrange(0,100))
special_char = random.choice(string.punctuation)
passwords=ad+no+number+special_char


root = Tk()

var = StringVar()
label = Label( root, textvariable=var)
var.set("Welcome to Password Generator")
label.pack()

var = StringVar()
label = Label( root, textvariable=var)
var.set("Your random generated password is:-")
label.pack()

var = StringVar()
label = Label( root, textvariable=var)
var.set(passwords)
label.pack()

B = Button(root, text ="Copy to clipboard?", command = helloCallBack)
B.pack()

root.mainloop()
    