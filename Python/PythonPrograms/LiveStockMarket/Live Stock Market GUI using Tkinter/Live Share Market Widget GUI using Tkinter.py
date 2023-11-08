from yahoo_fin import stock_info
from tkinter import *
from tkinter import messagebox
from time import *
import sys, os
import webbrowser
import threading
from share_list import l_sharelist

cwd = os.getcwd()

def HI():   
    

    def GOTo():
        webbrowser.open_new_tab("https://www.nuvamawealth.com/market/nse-option-chain")

    def SUBMIT_SHAREEE_1():
        class BackgroundTasks_1(threading.Thread):
            def run(self,*args,**kwargs):
                A=Share_TarEntry_1st_1.get()
                B=Share_TarEntry_2nd_1.get()
                C=Share_TarEntry_3rd_1.get()
                while 1+1==2:
                    price_TARGET1_1 = stock_info.get_live_price((Share_Input_1.get()))
                    check_1_1=str(price_TARGET1_1)
                    if check_1_1>A:
                        os.startfile("E:/Message1.mp3")
                        break
                    continue             
                             
                    if check_1_1>B:
                        os.startfile("E:/Message1.mp3")
                        break
                    continue  
                            
                            
                    if check_1_1>C:
                        os.startfile("E:/Message1.mp3")
                        break
                    continue 

        share1background=BackgroundTasks_1()
        share1background.start()

    def SUBMIT_SHAREEE_2():
        class BackgroundTasks_2(threading.Thread):
            def run(self,*args,**kwargs):
                AA=Share_TarEntry_1st_2.get()
                BB=Share_TarEntry_2nd_2.get()
                CC=Share_TarEntry_3rd_2.get()
                while 1+1==2:
                    price_TARGET1_2 = stock_info.get_live_price((Share_Input_2.get()))
                    check_1_2=str(price_TARGET1_2)
                    if check_1_2>AA:
                        os.startfile("E:/Message2.mp3")
                        break
                    continue             
                            
                    if check_1_2>BB:
                        os.startfile("E:/Message2.mp3")
                        break
                    continue  
                        
                        
                    if check_1_2>CC:
                        os.startfile("E:/Message3.mp3")
                        break
                    continue

        share2background=BackgroundTasks_2()
        share2background.start()
            

    def SUBMIT_SHAREEE_3():
        class BackgroundTasks_3(threading.Thread):
            def run(self,*args,**kwargs):
                AAA=Share_TarEntry_1st_3.get()
                BBB=Share_TarEntry_2nd_3.get()
                CCC=Share_TarEntry_3rd_3.get()
                while 1+1==2:
                    price_TARGET1_3 = stock_info.get_live_price((Share_Input_3.get()))
                    check_1_1=str(price_TARGET1_3)
                    if check_1_1>AAA:
                        os.startfile("E:/Message3.mp3")
                        break
                    continue             
                            
                    if check_1_1>BBB:
                        os.startfile("E:/Message3.mp3")
                        break
                    continue  

                
                    if check_1_1>CCC:
                        os.startfile("E:/Message3.mp3")
                        break
                    continue 

        share3background=BackgroundTasks_3()
        share3background.start()
    
    def SUBMIT_SHAREEE_4():
        class BackgroundTasks_4(threading.Thread):
            def run(self,*args,**kwargs):
                AAAA=Share_TarEntry_1st_4.get()
                BBBB=Share_TarEntry_2nd_4.get()
                CCCC=Share_TarEntry_3rd_4.get()
                while 1+1==2:
                    price_TARGET1_4 = stock_info.get_live_price((Share_Input_4.get()))
                    check_1_1=str(price_TARGET1_4)
                    if check_1_1>AAAA:
                        os.startfile("E:/Message4.mp3")
                        break
                    continue             
                            
                    if check_1_1>BBBB:
                        os.startfile("E:/Message4.mp3")
                        break
                    continue  
                    

                    if check_1_1>CCCC:
                        os.startfile("E:/Message4.mp3")
                        break
                    continue 

        share4background=BackgroundTasks_4()
        share4background.start()

    def SUBMIT_SHAREEE_5():
        class BackgroundTasks_5(threading.Thread):
            def run(self,*args,**kwargs):
                AAAAA=Share_TarEntry_1st_5.get()
                BBBBB=Share_TarEntry_2nd_5.get()
                CCCCC=Share_TarEntry_3rd_5.get()
                while 1+1==2:
                    price_TARGET1_5 = stock_info.get_live_price((Share_Input_5.get()))
                    check_1_1=str(price_TARGET1_5)
                    if check_1_1>AAAAA:
                        os.startfile("E:/Message5.mp3")
                        break
                    continue             
                            
                    if check_1_1>BBBBB:
                        os.startfile("E:/Message5.mp3")
                        break
                    continue    
                        
                    if check_1_1>CCCCC:
                        os.startfile("E:/Message5.mp3")
                        break
                    continue 

        share5background=BackgroundTasks_5()
        share5background.start()

    def stock_price_1():
        class BackgroundTasks_SHARE1(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Share_Input_1.get()))
                        Current_stock1.set(price)
                    except:
                        if Share_Input_1.get() == "":
                            break
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
                
        share1pricebackground=BackgroundTasks_SHARE1()
        share1pricebackground.start()
        
    def stock_price_2():
        class BackgroundTasks_SHARE2(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Share_Input_2.get()))
                        Current_stock2.set(price)
                    except:
                        if Share_Input_2.get() == "":
                            break
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
        share2pricebackground=BackgroundTasks_SHARE2()
        share2pricebackground.start()
    
    def stock_price_3():
        class BackgroundTasks_SHARE3(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Share_Input_3.get()))
                        Current_stock3.set(price)
                    except:
                        if Share_Input_3.get() == "":
                            break
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
        share3pricebackground=BackgroundTasks_SHARE3()
        share3pricebackground.start()

    def stock_price():
        class BackgroundTasks_SHAREsearch(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Search.get()))
                        Current_stock.set(price)
                    except:
                        if Share_Input_4.get() == "":
                            break
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
        sharepricebackground=BackgroundTasks_SHAREsearch()
        sharepricebackground.start()

    def stock_price_4():
        class BackgroundTasks_SHARE4(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Share_Input_4.get()))
                        Current_stock4.set(price)
                    except:
                        if Share_Input_5.get() == "":
                            break
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
        share4pricebackground=BackgroundTasks_SHARE4()
        share4pricebackground.start()

    def stock_price_5():
        class BackgroundTasks_SHARE5(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    try:
                        price = stock_info.get_live_price((Share_Input_5.get()))
                        Current_stock5.set(price)
                    except:
                        if price == "":
                            pass
                        else:
                            messagebox.showerror("Error", "Share not found")
                            break
        share5pricebackground=BackgroundTasks_SHARE5()
        share5pricebackground.start()

    def add_to_portfolio():
        pass

    def checkkey(event):
        value = event.widget.get()
        
        # get data from l
        if value == '':
            data = l_sharelist
        else:
            data = []
            for item in l_sharelist:
                if value.lower() in item.lower():
                    data.append(item)				

        # update data in listbox
        update(data)


    def update(data):
        
        # clear previous data
        Shares.delete(0, 'end')

        # put new data
        for item in data:
            Shares.insert('end', item)
    



    master = Tk()
    master.title('Live Stock Market Widget')
    master.state('zoomed')

    Current_stock = StringVar()
    Current_stock1 = StringVar()
    Current_stock2 = StringVar()
    Current_stock3 = StringVar()
    Current_stock4 = StringVar()
    Current_stock5 = StringVar()

    Share_Info_1 = Label(master, text="Share Symbol : ").grid(row=0, sticky=W)
    Share_Price_1 = Label(master, text="Share Price:").grid(row=6, sticky=W)
    Share_Input_1 = Entry(master)
    Share_Input_1.grid(row=0, column=1)
    result1 = Label(master, text="", textvariable=Current_stock1).grid(row=6, column=1, sticky=W)
    b1 = Button(master, text="Show", command=stock_price_1)
    b1.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
    Share_Target_1st_1=Label(master, text="Enter first target : ").grid(row=10, sticky=W)
    Share_TarEntry_1st_1=Entry(master)
    Share_TarEntry_1st_1.grid(row=10, column=1)
    Share_Target_2nd_1=Label(master, text="Enter second target : ").grid(row=11, sticky=W)
    Share_TarEntry_2nd_1=Entry(master)
    Share_TarEntry_2nd_1.grid(row=11, column=1)
    Share_Target_3rd_1=Label(master, text="Enter third target : ").grid(row=12, sticky=W)
    Share_TarEntry_3rd_1=Entry(master)
    Share_TarEntry_3rd_1.grid(row=12, column=1)
    Submit_Share1=Button(master, text="Submit Data for Share 1", command=SUBMIT_SHAREEE_1)
    Submit_Share1.place(x=10, y=140)

    Share_Info_2 = Label(master, text="Share Symbol : ").place(x=350, y=0)
    Share_Price_2 = Label(master, text="Share Price:").place(x=350, y=30)
    Share_Input_2 = Entry(master)
    Share_Input_2.place(x=470, y=0)
    result2 = Label(master, text="", textvariable=Current_stock2).place(x=470, y=30)
    b2 = Button(master, text="Show", command=stock_price_2)
    b2.place(x=600, y=0)
    Share_Target_1st_2=Label(master, text="Enter first target : ").place(x=350, y=60)
    Share_TarEntry_1st_2=Entry(master)
    Share_TarEntry_1st_2.place(x=470, y=60)
    Share_Target_2nd_2=Label(master, text="Enter second target : ").place(x=350, y=80)
    Share_TarEntry_2nd_2=Entry(master)
    Share_TarEntry_2nd_2.place(x=470, y=80)
    Share_Target_3rd_2=Label(master, text="Enter third target : ").place(x=350, y=100)
    Share_TarEntry_3rd_2=Entry(master)
    Share_TarEntry_3rd_2.place(x=470, y=100)
    Submit_Share2=Button(master, text="Submit Data for Share 2", command=SUBMIT_SHAREEE_2)
    Submit_Share2.place(x=370, y=140)

    Share_Info_3 = Label(master, text="Share Symbol : ").place(x=700, y=0)
    Share_Price_3 = Label(master, text="Share Price:").place(x=700, y=30)
    Share_Input_3 = Entry(master)
    Share_Input_3.place(x=820, y=0)
    result3 = Label(master, text="", textvariable=Current_stock3).place(x=820, y=30)
    b3 = Button(master, text="Show", command=stock_price_3)
    b3.place(x=950, y=0)
    Share_Target_1st_3=Label(master, text="Enter first target : ").place(x=700, y=60)
    Share_TarEntry_1st_3=Entry(master)
    Share_TarEntry_1st_3.place(x=820, y=60)
    Share_Target_2nd_3=Label(master, text="Enter second target : ").place(x=700, y=80)
    Share_TarEntry_2nd_3=Entry(master)
    Share_TarEntry_2nd_3.place(x=820, y=80)
    Share_Target_3rd_3=Label(master, text="Enter third target : ").place(x=700, y=100)
    Share_TarEntry_3rd_3=Entry(master)
    Share_TarEntry_3rd_3.place(x=820, y=100)
    Submit_Share3=Button(master, text="Submit Data for Share 3", command=SUBMIT_SHAREEE_3)
    Submit_Share3.place(x=720, y=140)

    Divider_1_4 = Label(master, text=" | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n|").place(x=295, y=290)
    Share_Info_4 = Label(master, text="Share Symbol : ").place(x=0, y=290)
    Share_Price_4 = Label(master, text="Share Price:").place(x=0, y=320)
    Share_Input_4 = Entry(master)
    Share_Input_4.place(x=115, y=290)
    result4 = Label(master, text="", textvariable=Current_stock4).place(x=115, y=320)
    b4 = Button(master, text="Show", command=stock_price_4)
    b4.place(x=245, y=290)
    Share_Target_1st_4=Label(master, text="Enter first target : ").place(x=0, y=345)
    Share_TarEntry_1st_4=Entry(master)
    Share_TarEntry_1st_4.place(x=115, y=345)
    Share_Target_2nd_4=Label(master, text="Enter second target : ").place(x=0, y=370)
    Share_TarEntry_2nd_4=Entry(master)
    Share_TarEntry_2nd_4.place(x=115, y=370)
    Share_Target_3rd_4=Label(master, text="Enter third target : ").place(x=0, y=395)
    Share_TarEntry_3rd_4=Entry(master)
    Share_TarEntry_3rd_4.place(x=115, y=395)
    Submit_Share4=Button(master, text="Submit Data for Share 4", command=SUBMIT_SHAREEE_4)
    Submit_Share4.place(x=8, y=425)

    Label(master, text="🔍 Search for Shares").place(x=320, y=290)
    Search=Entry(master)
    Search.bind('<KeyRelease>', checkkey)
    Search.place(x=500, y=290)
    GET=Button(master, text="Show", command=stock_price).place(x=700, y=290)
    Shares = Listbox(master)
    Shares.place(x=500, y=320)
    update(l_sharelist)
    PRICE=Label(master, text="", textvariable=Current_stock).place(x=500, y=500)
    Label(master, text="🔍 Search for Options").place(x=320, y=530)
    Options=Button(master, text="Go to Options", command=GOTo)
    Options.place(x=500, y=530)

    Divider_1_5 = Label(master, text=" | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n|").place(x=760, y=290)
    Share_Info_5 = Label(master, text="Share Symbol : ").place(x=790, y=290)
    Share_Price_5 = Label(master, text="Share Price:").place(x=790, y=320)
    Share_Input_5 = Entry(master)
    Share_Input_5.place(x=900, y=290)
    result5 = Label(master, text="", textvariable=Current_stock5).place(x=905, y=320)
    b5 = Button(master, text="Show", command=stock_price_5)
    b5.place(x=1035, y=290)
    Share_Target_1st_5=Label(master, text="Enter first target : ").place(x=790, y=345)
    Share_TarEntry_1st_5=Entry(master)
    Share_TarEntry_1st_5.place(x=905, y=345)
    Share_Target_2nd_5=Label(master, text="Enter second target : ").place(x=790, y=370)
    Share_TarEntry_2nd_5=Entry(master)
    Share_TarEntry_2nd_5.place(x=905, y=370)
    Share_Target_3rd_5=Label(master, text="Enter third target : ").place(x=790, y=395)
    Share_TarEntry_3rd_5=Entry(master)
    Share_TarEntry_3rd_5.place(x=905, y=395)
    Submit_Share5=Button(master, text="Submit Data for Share 5", command=SUBMIT_SHAREEE_5)
    Submit_Share5.place(x=798, y=425)
    
    Add_to_Portfolio_Button = Button(master, text="+ Add Shares to Portfolio", command=add_to_portfolio).place(x=1010, y=600)
    
    master.mainloop()

    

HI()
