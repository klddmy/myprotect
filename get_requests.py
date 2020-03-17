import requests
from  bs4   import BeautifulSoup


url="http://www.cntour.cn"

response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,'lxml')
data=soup.select("#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(4) > a:nth-child(1)")
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)