#Welcome to Dynapite - The App Builder For Dynomo. Build Apps for Dynomo with this App. 

#Version = Version 5

#Imports
from tkinter import *
import os
from tkinter import filedialog as fd
global filenameforexecuting
filenameforexecuting = ""

#Defines
def OPENFILE():
    file_path = fd.askopenfilename(
                filetypes=(
                    ("Dyn Programming Files", "*.dyn"),
                    ("All Files", "*.*")
                )
            )

    split_tup = os.path.splitext(file_path)
    file_name = split_tup[0]
    forcop = file_name
    file_extension = split_tup[1]
    forex = ".py"
    completedirforrwname = forcop + forex
    if file_extension==".dyn":
        with open(file_path) as f:
            contents = f.read()
            my_file = file_path
            base = os.path.splitext(my_file)[0]
            f.close()
            os.rename(my_file, base + '.py')
            try:
                exec(contents)
                status1 = Label(window, text="Script Succeeded. Good Work!\nIn Dynomo, open Dynomo and launch Dynapite in Dynomo. Open the .dyn file which was generated now\n and, your App is ready on Dynomo", bg="#E1AE0E").place(x=650, y=100)
                my_file = completedirforrwname
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.dyn')
            except Exception as e:
                print("Failed")
                status1 = Label(window, text="Script Failed. Try Again!", bg="#E1AE0E").place(x=650, y=100)
                my_file = completedirforrwname
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.dyn')
    else:
        status1 = Label(window, text="Unable to Open", bg="#E1AE0E").place(x=650, y=100)

def SAVEFILE():
    code=EnterScript.get("1.0",'end-1c')
    file_path = fd.asksaveasfilename(
                filetypes=(
                    ("Dyn Programming Files", "*.dyn"),
                )
            )
    if file_path == "":
        pass
    else:
        finaldir=f"{file_path}.dyn"
        with open(finaldir, 'w') as f:
            f.write(code)

def CHECK():
    subject = EnterScript.get("1.0",'end-1c')
    try:
        exec(subject)
        status = Label(window, text="Script Succeeded. Good Work!", bg="#E1AE0E").place(x=50, y=440)
        SaveFile = Button(window, text="Save your file", command=SAVEFILE)
        SaveFile.place(x=50, y=460)
    except Exception as e:
        status = Label(window, text="Script Failed. Try Again!", bg="#E1AE0E").place(x=50, y=440)

#Main Code
window = Tk()
window.state("zoomed")
window.configure(bg="#E1AE0E")
window.title("Dynapite - The App Builder For Dynomo")

MainLabel = Label(window, text="Welcome to Dynapite - The App Builder For Dynomo", bg="#E1AE0E")
MainLabel.place(x=520, y=0)

EnterCode = Label(window, text="Enter your Python Script to build in Dynomo. We will make suitable amends to make this app work in Dynomo", bg="#E1AE0E")
EnterCode.place(x=5, y=40)
EnterScript = Text(window)
EnterScript.place(x=5, y=70,width=600,height=300)
Check = Button(window, text="Check Code", command=CHECK)
Check.place(x=50, y=400)

OpenCode = Label(window, text="Open your Python Script to build in Dynomo. We will make suitable amends to make this app work in Dynomo", bg="#E1AE0E")
OpenCode.place(x=650, y=40)
OPENButton = Button(window, text="Open File and Execute", command=OPENFILE)
OPENButton.place(x=650, y=70)

#Mainloop
window.mainloop()