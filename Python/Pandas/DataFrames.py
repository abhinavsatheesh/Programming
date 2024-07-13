import pandas as pd
Sales = pd.DataFrame({2014:[100.5,150.8,200.9,30000,40000], 2015:[12000,18000,22000,30000,45000], 2016:[20000,50000,70000,100000,125000], 2017:[50000,60000,70000,80000,90000]}, index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
#Display row labels
print(Sales.index)
#Display column labels
print(Sales.columns)
#Display data types of each column
print(Sales.dtypes)
#Display dimensions, shape, size, values
print(Sales.ndim)
print(Sales.shape)
print(Sales.size)
print(Sales.values)
#Display last 2 rows
print(Sales.tail(2))
#Display first 2 columns
print(Sales.iloc[:,0:2])

#Create dictionary using this data, and using this create dataframe sales2
dic = {2018:[160000,110000,500000,340000,900000]}
Sales2 = pd.DataFrame(dic, index = Sales.index)
print(Sales2)
#Check if sales2 is empty or not
print(Sales2.empty)

#Append Sales2 to Sales
Sales = pd.concat([Sales,Sales2], axis = 1)
print(Sales)

#Transpose Sales
print(Sales.T)

#Display sales made in 2017
print(Sales[2017])
#Display sales made by Madhu and Ankit in 2017 and 2018
print(Sales.loc[["Madhu","Ankit"],[2017,2018]])
#Display sales made by Shruti in 2016
print(Sales.loc["Shruti",2016])
#Adding data
Sales.loc["Sumeet"]=[196.2,37800,52000,78438,38852]
print(Sales)
#Display data for 2014
print(Sales[2014])
#Display data for Kinshuk
print(Sales.loc['Kinshuk'])
#Renaming data
Sales.rename({"Ankit":"Vivaan","Madhu":"Shailesh"}, axis = 0, inplace=True)
print(Sales)
#Updating data
Sales.loc['Shailesh',2018]=100000
print(Sales)
#Writing to a CSV
Sales.to_csv("SalesFigures.csv", header=False, index=False)
print("Saved successfully")
#Reading from CSV
SalesRetrieved = pd.read_csv("SalesFigures.csv", header = None)
print(SalesRetrieved)
SalesRetrieved.columns = Sales.columns
SalesRetrieved.index = Sales.index
print(SalesRetrieved)
