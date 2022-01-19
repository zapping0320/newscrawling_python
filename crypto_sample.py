import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=암호화폐 세금",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

articles = html.select("ul.list_news > li")

#print(articles[0])
for ar in articles:
    titles = ar.select('li > div > div > a')
    for title in titles:
        print(titles[0].get_text())

#clips = articles[0].select_one("news_area")#"news_wrap api_ani_send")

#print(clips)

#inner1 = clips[0].select_one("news_area")

#print(inner1)

# 첫번째 기사에 대한 제목/언론사를 수집해서 출력합니다.
#title = articles[0].select_one("a.href").text``
#source = articles[0].select_one("span._sp_each_source").text

#print(title, source)