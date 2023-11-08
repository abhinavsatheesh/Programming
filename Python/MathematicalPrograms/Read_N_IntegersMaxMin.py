print("Program to read n integers and display maximum and minimum nos. from that set")
n=int(input("Enter no. of values you will be entering"))
no=0
no_min=0
for i in range(n):
    i=int(input())
    if i>no:
        no=i
    if i<no:
        no_min=i
print(f"Maximum no. from the set of numbers : {no}")
print(f"Minimum no. from the set of numbers : {no_min}")
