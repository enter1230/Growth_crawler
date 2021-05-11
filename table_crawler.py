from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib

html=urlopen("http://www.index.go.kr/unify/idx-info.do?idxCd=4201")

soup=BeautifulSoup(html, "lxml")

growth_year=soup.find_all('thead')
growth_content=soup.find_all('tbody')

html=urlopen("http://www.index.go.kr/unify/idx-info.do?idxCd=4227")

soup=BeautifulSoup(html, "lxml")

year_table = soup.find_all('thead')
people_table = soup.find_all('tbody')
#경제성장률 리스트

year_info=[]
for tr in growth_year:
    value1_info=[]
    th=tr.find_all('th')
    print(th)
    print(len(th))
    print('')
    for content in th:
        print(content.get_text(),end=', ')
        value1_info.append(content.get_text())
    print('')
    year_info.append(value1_info)
print('')

content_info=[]
for tr in growth_content:
    value2_info=[]
    td=tr.find_all('td')
    print(td)
    print(len(td))
    print('')
    for content in td:
        print(content.get_text(),end=', ')
        value2_info.append(content.get_text())
    print('')
    content_info.append(value2_info)
print('')

year_list=[]
for i in range(1,15):
    year_list.append(value1_info[i])
print(year_list)
content_list=[]
for i in range(14):
    content_list.append(value2_info[i])
print(content_list)


#인구성장률 리스트
people_temp_info=[]
for tr in people_table:
    value_temp_info=[]
    td=tr.find_all("td")
    print(td)
    print(len(td))
    print("")

    for content in td:
        print(content.get_text(), end=', ')
        value_temp_info.append(content.get_text())
    print("")
    people_temp_info.append(value_temp_info)
print("")

peoples_temp_info=[]
for tr in year_table:
    values_temp_info=[]
    th=tr.find_all("th")
    print(th)
    print(len(th))
    print("")

    for content in th:
        print(content.get_text(), end=', ')
        values_temp_info.append(content.get_text())
    print("")
    people_temp_info.append(values_temp_info)
print("")

value_list=[]

for i in range(14):
    value_list.append(value_temp_info[i])

print(value_list)

values_list=[]

for i in range(1,15):
    values_list.append(values_temp_info[i])

print(values_list)



matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
plt.bar(x,value_list)
plt.xticks(x,values_list)
plt.suptitle('인구성장률')
plt.xlabel('년도')
plt.ylabel('성장률')


plt.show()