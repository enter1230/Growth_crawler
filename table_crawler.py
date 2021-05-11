from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.index.go.kr/unify/idx-info.do?idxCd=4201")

soup=BeautifulSoup(html, "lxml")

growth_year=soup.find_all('thead')
growth_content=soup.find_all('tbody')

html=urlopen("http://www.index.go.kr/unify/idx-info.do?idxCd=4227")

soup=BeautifulSoup(html, "lxml")

year_table = soup.find_all('thead')
people_table = soup.find_all('tbody')