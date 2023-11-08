ques=input('Do you wish to find the Volume of Cube by 2D Method or via Side Method? Please enter either 2D or Side')
if ques=='2D':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='Side':
    print ('OK.')
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
else:
    exit()