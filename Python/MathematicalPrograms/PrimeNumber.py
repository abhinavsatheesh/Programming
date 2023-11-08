num=int (input('Enter a number between 2 and 10.'))
if num > 10 or num<2:
    print('This is a number off limits. Retry again.')
else:
    if num%2 == 0 and num>2:
        print(f'{number} is not a prime number')
    elif num%3 == 0 and num!= 3:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is a prime number')
