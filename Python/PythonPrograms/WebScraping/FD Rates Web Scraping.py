def getDays(text):
    t=text.lower().lstrip('\r').replace('%','').lstrip().replace('\r','')
    #print(f'|{t}|')

    try:
        l=float(t)
    except:
        l=t
    
    return l

def getHDFC_FD():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    URL='https://www.hdfcbank.com/personal/resources/rates#/fixed-deposit-interest-rate-less-than-5-cr'

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    selector='div.rates-heading ~ div.rates-body'
    fdSection = soup.select(selector)[0]
    fdTable=fdSection.find_all("table")[0]
    #print(fdTable)
     
    fdTableRows=fdTable.find_all("tr")
    #print(fdTableRows)

    fdd=[]
    for fdRow in fdTableRows:
        li=[]
        for idx,data in enumerate(fdRow.find_all("td")):
            if idx<3:
                d=data.text.rstrip("\n")
                d=getDays(d)
                li.append(d)
        fdd.append(li)
    fdData=[]
    for d in fdd:
        if len(d)>0:
            fdData.append(d)

    return fdData

def getHDFC_RD():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    URL='https://www.hdfcbank.com/personal/resources/rates#/fixed-deposit-interest-rate-less-than-5-cr'

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    selector='div.rates-heading ~ div.rates-body'
    rdSection = soup.select(selector)[1]
    rdTable=rdSection.find_all("table")[0]
    #print(rdTable)
     
    rdTableRows=rdTable.find_all("tr")
    #print(rdTableRows)

    rdd=[]
    for rdRow in rdTableRows:
        li=[]
        for idx,data in enumerate(rdRow.find_all("td")):
            if idx<3:
                d=data.text.rstrip("\n")
                d=getDays(d)
                li.append(d)
        rdd.append(li)
    rdData=[]
    for d in rdd:
        if len(d)>0:
            rdData.append(d)

    return rdData

def getICICI_FD():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    URL='https://www.icicibank.com/Personal-Banking/account-deposit/fixed-deposit/fd-interest-rates.page?#toptitle'

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())
    #table-container

    selector='div.table-container > table'
    fdSection = soup.select(selector)[0]
    fdTableRows=fdSection.find_all("tr")
    #print(fdTable)

    fdd=[]
    for fdRow in fdTableRows:
        li=[]
        for idx,data in enumerate(fdRow.find_all("td")):
            if idx<3:
                d=data.text.rstrip("\n")
                d=getDays(d)
                li.append(d)
        fdd.append(li)
    fdData=[]
    for d in fdd:
        if len(d)>0:
            fdData.append(d)

    return fdData

def getICICI_RD():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    URL='https://www.icicibank.com/Personal-Banking/account-deposit/recurring-deposits/rd-interest-rate.page?#toptitle'

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    selector='div.table-container'
    rdSection = soup.select(selector)[0]
    rdTable=rdSection.find_all("table")[0]
    #print(rdTable)
     
    rdTableRows=rdTable.find_all("tr")
    #print(rdTableRows)

    rdd=[]
    for rdRow in rdTableRows:
        li=[]
        for idx,data in enumerate(rdRow.find_all("td")):
            if idx<3:
                d=data.text.rstrip("\n")
                d=getDays(d)
                li.append(d)
        rdd.append(li)
    rdData=[]
    for d in rdd:
        if len(d)>0:
            rdData.append(d)

    return rdData

def getPNB_FD():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    URL='https://www.pnbindia.in/Interest-Rates-Deposit.html'

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    selector='h2#pnbsugamscheme ~ table.inner-page-table'
    fdSection = soup.select(selector)[0]
     
    fdTableRows=fdSection.find_all("tr")
    #print(fdTableRows)

    fdd=[]
    for jdx,fdRow in enumerate(fdTableRows):
        li=[]
        if jdx==1: continue#first row (2nd tr) has heading in td
        for idx,data in enumerate(fdRow.find_all("td")):
            if idx in (1,2,4):
                d=data.text.rstrip("\n")
                d=getDays(d)
                li.append(d)
        fdd.append(li)
    fdData=[]
    for d in fdd:
        if len(d)>0:
            fdData.append(d)

    return fdData

data={}
data['HDFC Bank FD Rates']=getHDFC_FD()
data['ICICI Bank FD Rates']=getICICI_FD()
data['PNB FD Rates']=getPNB_FD()

#print(data)

import json
jsondata=json.dumps(data)
#print(jsondata)

with open("bank.json", 'w') as file:
    json_data = jsondata
   
    json_object = json.loads(json_data)
       
    # Indent keyword while dumping the
    # data decides to what level 
    # spaces the user wants.
    finaldata = json.dumps(json_object, indent = 1)
    file.write(finaldata)