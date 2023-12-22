from bs4 import BeautifulSoup
from pprint import pprint
import requests
 
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()
 
data1 = soup.find('div',{'class':'col_inner'})
#pprint(data1)
 
data2 = data1.findAll('a',{'class':'title'})
#pprint(data2)
 
title_list1 = []
for t in data2:
    title_list1.append(t.text)
#pprint(title_list1)
 
 
title_list2 = [t.text for t in data2]
#pprint(title_list2)
 
data_list = soup.findAll('div',{'class':'col_inner'})
 
week_title_list = []
 
for divisionData1 in data_list:
    divisionData2 = divisionData1.findAll('a',{'class':'title'})
    #pprint(divisionData2)
    title_list3 = [t.text for t in divisionData2]
    #pprint(title_list3)
    #week_title_list.extend(title_list3) 1차원
    week_title_list.append(title_list3)
 
pprint(week_title_list)
