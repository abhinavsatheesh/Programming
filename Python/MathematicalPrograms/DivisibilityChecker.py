#Program to check whether a number is divisible by a number or not
a=int(input('Enter a number'))
b=int(input(f"Enter another number by which we should check if {a} is divisble"))
if a%b==0:
    print ('Your number', a,' is divisible by',b)
else:
    print ('Your number', a,'is not divisible by',b)
