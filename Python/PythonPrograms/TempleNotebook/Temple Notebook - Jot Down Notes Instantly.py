#Welcome to Temple Notebook, my last program using Python. I am making this program to help myself to write down the important details of each temple with ease
#So here we go, last program. 

#Imports:-
from tkinter import *
import anvil.server
from anvil.tables import app_tables

#Connect to Anvil Server:-
anvil.server.connect("CXSCRUM4KB7WZ6WRUJOSSIUT-SYTFMZXA4NXCKIOH-CLIENT")

#Defines:-  
def SUBMIT():
    STORY=TempleStory.get(1.0, "end-1c")
    debug(STORY)
    row = app_tables.temple_stories.add_row(TempleStories=STORY)
    
def debug(data):
    print (data)

#Main Code:-
MainPage=Tk()
MainPage.state("zoomed")
MainPage.title("Temple Notebook | Jot Down Notes Instantly")

#Blue Tip
DESIGN1=Label(MainPage, text="", fg='white', bg="#009EFF", width=700, height=4)
DESIGN1.pack()
DYNOMOD=Label(MainPage, text="Temple Notebook - Jot Down Notes Instantly", fg="white", bg="#009EFF", height=1, font=('Arial bold', 15))
DYNOMOD.place(x=50, y=15)

#Instructions Label and Text
Instructions=Label(MainPage, text="Copy the notes of Temple in your Samsung Notes and paste it here")
Instructions.place(x=150, y=80)
TempleStory=Text(MainPage)
TempleStory.place(x=150, y=120)

#Submit Button
Submit=Button(MainPage, text="SUBMIT", fg="#009EFF", command=SUBMIT)
Submit.place(x=500, y=550)


#Mainloop
MainPage.mainloop()