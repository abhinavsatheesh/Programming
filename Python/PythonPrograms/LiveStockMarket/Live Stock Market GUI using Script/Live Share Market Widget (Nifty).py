from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import webbrowser
import time
import sys, os
import struct
import time


print ('Welcome to Live Stock Market Widget created by Abhinav Satheesh')


def get_Nifty50_CURRENTPRICE(URL):
    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    selector='div#indices_price span#cp'
    data=soup.select(selector)
    print (f'Current price of Nifty50 is {data[0].getText()}')

def NEW_CREATION():
  print ('Welcome to the New User Creation Panel')
  us=input('Enter a username')
  print ('Username validated successfully')
  password=str(input('Enter a password or if you wish to create a random password, enter 1'))
  if password=='1':
    import string
    import random
    import sys
    adjectives = ['enormous', 'doglike', 'silly', 'yellow', 'fun', 'fast', 'beautiful', 'sleepy', 'slow', 'smelly','wet', 'fat', 'red','orange', 'yellow', 'green', 'blue', 'purple', 'fluffy','white', 'proud', 'brave', 'adorable', 'amused', 'annoying', 'ashamed', 'awful', 'better', 'bloody', 'blushing', 'brave', 'busy']
    nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda', 'more', 'some ', 'telephone', 'banana', 'teacher']
    while True:
      ad=random.choice(adjectives)
      no=random.choice(nouns)
      number=str(random.randrange(0,100))
      special_char = random.choice(string.punctuation)
      password=ad+no+number+special_char
      print ('Generated password is', password)
      question=input('Do you need another password? Type y or n')
      if question == 'n':
        print ('Account created successfully. Login again')
        user[us]=password
        complete='completed'
        login()
      if question =='y':
        print ('OK.')
        ad=random.choice(adjectives)
        no=random.choice(nouns)
        number=str(random.randrange(0,100))
        special_char = random.choice(string.punctuation)
        password=ad+no+number+special_char
        print ('Your new password is', password)
        question=input('Do you need another password? Type y or n')
        
def login():
  for x in range(0,1):
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
      continue
    elif username not in user:
      print("This is not a valid username, input username again!")
      continue
    elif password != user[username]:
      print(f"Password is not valid for {username}. ")
      continue
    elif password == user[username]:
      print(f"Welcome {username} ")
      print(f"Thank you for logging on. ")
      complete = True
      get_Nifty50_CURRENTPRICE('https://www.moneycontrol.com/')
      for x in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        time.sleep(600)
        get_Nifty50_CURRENTPRICE('https://www.moneycontrol.com/')   

      
        
complete = False
user = {"abhinav_s":"abhinav07",
"admin":"developer",
"satheesh_b" : "abhinav07", 
"anu_satheesh" : "abhinav07", 
"ananthan":"17dec2015", 
"lakshmi_n":"abhi0607"}

while not complete:
    print ('Enter new in username and password if you wish to create a new account')
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
      continue
    elif username not in user:
      if username=='new' and password=='new':
        NEW_CREATION()
      else:
        print("This is not a valid username, input username again!")
        continue     
      
    elif password != user[username]:
      print(f"Password is not valid for {username}. ")
      continue
    elif password == user[username]:
      print(f"Welcome {username} ")
      print(f"Thank you for logging on. ")
      complete = True
      get_Nifty50_CURRENTPRICE('https://www.moneycontrol.com/')
      for x in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        time.sleep(600)
        get_Nifty50_CURRENTPRICE('https://www.moneycontrol.com/')

      
      

      
    
      
      
       

