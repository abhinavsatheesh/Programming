#Program to find Simple Interest
p=int(input('Enter the Principal amount'))
r=int(input('Enter the Rate of Interest in Numbers'))
t=int(input('Enter the Time in Years'))
SI=(p*r*t)/100
amount = p+SI
print ('Simple Interest = ₹', SI)
print ("Final Amount = ₹", amount)

