import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

people = soup.findAll('strong', {'class': 'num'})
data_list = []
for i in people:
    data_list.append(i.get_text().replace('\n', '').replace(' ', ''))
print("확진환자 " + data_list[0] + "\n격리해제 " + data_list[1] + "\n검사 진행 " + data_list[2] + "\n사망자 " + data_list[3])