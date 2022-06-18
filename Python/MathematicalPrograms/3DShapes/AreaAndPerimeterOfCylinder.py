import math
pi=math.pi
r=int(input('Enter the Radius'))
h=int(input('Enter the Height'))
c=2*pi*r
print ('Perimeter of the Bottom Circle is', c, "cm")
a=pi*r**2
print ('Area of the Bottom Circle is', a, "sq.cm.")
tsa=2*pi*r*(r+h)
print ('Total Surface Area of the Cylinder is', tsa, "sq.cm.")
lsa=2*pi*r*h
print ('Lateral Surface Area of the Cylinder is', lsa, "sq.cm.")