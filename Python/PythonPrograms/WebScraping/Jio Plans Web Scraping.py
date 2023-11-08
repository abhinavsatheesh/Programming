
jioURL='https://www.jio.com/en-in/4g-plans'

def getJioPrePaidSelection(URL):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")

    selector='div.jio-accordion h2 a'
    headings=data=soup.select(selector)
    data=[]
    for idx,h in enumerate(headings):
        data.append({f'header{idx}':h.getText()})

    return data


def getJioPrePaidPlan(URL, selection):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re

    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    
    headingSel=selection-1
    
    selector=f'div.jio-accordion div#heading{headingSel} + div.jio-accordion-body div.plan_details div.plan_detail_list span.MainPrice'
    data=data=soup.select(selector)
    
    pricedata=[]
    for d in data:
        pricedata.append(d.getText())
    
    selector=f'div.jio-accordion div#heading{headingSel} + div.jio-accordion-body div.plan_details div.plan_detail_list div.list_inline'
    data=soup.select(selector)
    #print(data)

    daysdata=[]
    for d in data:
        if 'days' in d.getText():
            dd=d.getText().replace('\n','').replace('days','')
            daysdata.append(dd)
    #merge price and days
    outdata=[]
    for idx,pd in enumerate(pricedata):
        perday=round(float(pd)/float(daysdata[idx]),2)
        outdata.append({'price':pd,'days':daysdata[idx],'cost_per_day':perday})
    outdata=sorted(outdata, key = lambda i: i['cost_per_day'])
    return outdata

plans=getJioPrePaidSelection(jioURL)
pricedata=[]
for idx,p in enumerate(plans):
    print(p)
    print(getJioPrePaidPlan(jioURL, idx+1))

