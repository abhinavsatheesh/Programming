#Welcome to Queue Manager, the App to control all your Queues
#Imports:-

from tkinter import *
import anvil.server
from anvil.tables import app_tables
import datetime
from dateutil.relativedelta import relativedelta
from time import *

#Connect to Anvil Server
anvil.server.connect("QNX44DGRMS4QSKW6YQICYSC3-OKYCDWTANXGWPMM4-CLIENT")

#Defines:-
def SUBMITDATA():
    one_year_from_now = datetime.datetime.now() + relativedelta(years=0)
    dt = one_year_from_now.strftime("%d/%m/%Y")
    NameTextH=Entry1.get()
    AgeTextT=Entry2.get()
    AgeTextH=int(AgeTextT)
    MobileNoTextT=Entry3.get()
    MobileNoTextH=int(MobileNoTextT)
    EmailIDTextH=Entry4.get()
    AddressTextH=Entry5.get("1.0",'end-1c')
    row = app_tables.user_management.add_row(NameText=NameTextH, AgeText=AgeTextH, MobileNumberText=MobileNoTextH, EmailIDText=EmailIDTextH, AddressText=AddressTextH, DateTimeText=dt)

#Tkinter Window:-
MainPage=Tk()
MainPage.title("Queue Manager")
MainPage.state("zoomed")

#Main Code:-

#Welcome Label:-
WelcomeLabel=Label(MainPage, text="Welcome to Queue Manager | The One App to Manage Your Queues")
WelcomeLabel.pack()

#Name Label and Entry:-
Label1=Label(MainPage, text="Enter the Name of the person")
Label1.place(x=100, y=50)
Entry1=Entry(MainPage)
Entry1.place(x=500, y=50)   

#Age Label and Entry:-
Label2=Label(MainPage, text="Enter the Age of the person")
Label2.place(x=100, y=100)
Entry2=Entry(MainPage)
Entry2.place(x=500, y=100) 

#Mobile Number Label and Entry:-
Label3=Label(MainPage, text="Enter the Mobile Number of the person")
Label3.place(x=100, y=150)
Entry3=Entry(MainPage)
Entry3.place(x=500, y=150)  

#Email ID Label and Entry:-
Label4=Label(MainPage, text="Enter the Email ID of the person")
Label4.place(x=100, y=200)
Entry4=Entry(MainPage)
Entry4.place(x=500, y=200)  

#Address Label and Entry:-
Label5=Label(MainPage, text="Enter the Address of the person")
Label5.place(x=100, y=250)
Entry5=Text(MainPage)
Entry5.place(x=500, y=250, width=400,height=200) 
  
#Submit Button
Submit=Button(MainPage, text="Submit", command=SUBMITDATA)
Submit.place(x=200, y=350)

#Mainloop:-
MainPage.mainloop()