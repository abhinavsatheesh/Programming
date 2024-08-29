import pandas as pd

#Dictionary of List
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
l1 = ["Abhinav","Satheesh", "Anu"]
l2 = [183,179,165]
l3 = [71,74,55]
d = {"Name":l1, "Height":l2, "Weight":l3}
df = pd.DataFrame(d)

#Dictionary of Dictionary
'''OUTPUT:
        d1     d2     d3
Name  Abhinav  Satheesh  Anu
Height     183      179   165
Weight     71      74    55
'''
d1 = {"Name":"Abhinav", "Height":183, "Weight":71}
d2 = {"Name":"Satheesh", "Height":179, "Weight":74}
d3 = {"Name":"Anu", "Height":165, "Weight":55}  
d = {"d1":d1, "d2":d2, "d3":d3}
df = pd.DataFrame(d)

#Dictionary of Series
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
s1 = pd.Series([183,179,165])
s2 = pd.Series([71,74,55])
s3 = pd.Series(["Abhinav","Satheesh","Anu"])
d = {"Height":s1, "Weight":s2, "Name":s3}   
df = pd.DataFrame(d)

#List of Dictionary
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
d1 = {"Name":"Abhinav", "Height":183, "Weight":71}
d2 = {"Name":"Satheesh", "Height":179, "Weight":74}
d3 = {"Name":"Anu", "Height":165, "Weight":55}
l = [d1, d2, d3]
df = pd.DataFrame(l)

#List of List
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
l1 = ["Abhinav","Satheesh", "Anu"]
l2 = [183,179,165]
l3 = [71,74,55]
l = [l1,l2,l3]
df = pd.DataFrame(l)
#List of Series
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
s1 = pd.Series([183,179,165])
s2 = pd.Series([71,74,55])
s3 = pd.Series(["Abhinav","Satheesh","Anu"])
df = pd.DataFrame([s3,s2,s1], index=['Name', 'Height', 'Weight'])
print(df)
#List of Tuples
'''OUTPUT:
    Name        Height  Weight
0   Abhinav     183     71
1   Satheesh    179     74
2   Anu         165     55
'''
t1 = ("Abhinav",183,71)
t2 = ("Satheesh",179,74)
t3 = ("Anu",165,55)
t = [t1,t2,t3]
df = pd.DataFrame(t, columns=["Name","Height","Weight"])
