ques=input('Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method? Please enter either 2D or 3D')
if ques=='2D':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='3D':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)

else:
    exit()