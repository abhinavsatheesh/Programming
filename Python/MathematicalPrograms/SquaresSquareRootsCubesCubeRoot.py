#Calculate the square, square root, cube of a number
import math
number1=int(input('Enter a number'))
sq=number1*number1
number2=int(input('Enter another number.' ))
cu=number2*number2*number2
root=int(input('Enter another number.'))
roots=math.sqrt(root)
x=int(input('Enter another number'))
def cube_root(x):
        return x**(1/3)
print ('The square of the number', number1,'=', sq)
print ('The cube of the number', number2, '=', cu)
print ('The square root of the number', root, '=', roots)
print('The cube root of the number',x,'=', cube_root(x))