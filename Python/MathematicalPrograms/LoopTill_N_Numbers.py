print("Program to print 'n' natural even numbers")
n=int(input("Enter the number upto which you need the output"))
for i in range(2, n+1, 2):
    print(i, end=", ")
print("\n")


print("Program to print 'n' natural odd numbers")
n=int(input("Enter the number upto which you need the output"))
for i in range(1, n+1, 2):
    print(i, end=", ")
print("\n")
print("End of Code")