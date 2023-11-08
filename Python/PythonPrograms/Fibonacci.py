n=int(input("Enter a number"))
if n==1:
    print(0)
else:
    first, second=0,1
    print(first, second, end=" ")
    x=3
    while x<=n:
        third = first+second
        print(third, end=" ")
        first, second = second, third
        x+=1
        
