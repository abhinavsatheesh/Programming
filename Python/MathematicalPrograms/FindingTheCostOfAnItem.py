#Finding the total cost of the item if quantity and price is given
name=input('Enter the name of the Item')
quantity=int(input('Enter the quantity of the Item. Enter in Kilograms'))
sprice=int(input('Enter the price of the Item'))
totalprice=quantity*sprice
print ('Total Price for the item',name, 'is Rs.',totalprice)
