principal=int(input("Enter the Principal amount"))
year=int(input("Enter the no. of Years"))
rateofinterest=int(input("Enter the Rate of Interest. Just enter the number"))
amount=principal*((1+rateofinterest/100)**year)
compoundinterest = amount-principal
print(f"Compound Interest is {compoundinterest} Rupees")
print(f"Amount is {amount} Rupees")
