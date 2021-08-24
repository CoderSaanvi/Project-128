from bs4 import BeautifulSoup
import pandas as pd
import requests
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(START_URL)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
starTable=soup.find_all('table')
print(len(starTable))
temp_list=[]
tableRows=starTable[4].find_all('tr')

for tr in tableRows: 
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)

print(temp_list)

starNames=[]
distance=[]
radius=[]
mass=[]

for i in range(1,len(temp_list)): 
    starNames.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])

df2=pd.DataFrame(list(zip(starNames,distance,mass,radius)),columns=['Star Names','Distance','Mass','Radius'])
print(df2)
df2.to_csv('dwarf.csv')
