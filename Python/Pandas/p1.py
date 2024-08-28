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

#List of Dictionary
'''OUTPUT
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