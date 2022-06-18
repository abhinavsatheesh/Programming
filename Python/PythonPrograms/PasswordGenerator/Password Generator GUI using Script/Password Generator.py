import string
import random
import sys
from Adjectives import adjectives as adject
from Nouns import nouns as nou
while True:
    ad=random.choice(adject)
    no=random.choice(nou)
    number=str(random.randrange(0,100))
    special_char = random.choice(string.punctuation)
    password=ad+no+number+special_char
    print ('Hello. Welcome to Password Picker.')
    print ('Your new password is', password)
    question=input('Do you need another password? Type y or n')
    if question == 'n':
        break
    if question =='y':
        print ('OK.')
        ad=random.choice(adject)
        no=random.choice(nou)
        number=str(random.randrange(0,100))
        special_char = random.choice(string.punctuation)
        password=ad+no+number+special_char
        print ('Your new password is', password)
        question=input('Do you need another password? Type y or n')
    else:
        print ('That is an incorrect option. Please try again')
        question=input('Do you need another password? Type y or n')