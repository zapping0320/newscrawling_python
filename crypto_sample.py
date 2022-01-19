import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=암호화폐 세금",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

articles = html.select("ul.list_news > li")

#print(articles[0])
for ar in articles:
    times  = ar.select('li > div > div > div > div > span')
    print(times[0].get_text())

    titles = ar.select('li > div > div > a')
    print(titles[0].get_text())
    print(titles[0]["href"])
    

