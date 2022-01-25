import requests
from bs4 import BeautifulSoup

token = "{token}"
channel = "#news_crawler01"

raw = requests.get("https://search.naver.com/search.naver?where=news&query=암호화폐 세금",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

articles = html.select("ul.list_news > li")

for ar in articles:
    times  = ar.select('li > div > div > div > div > span')
    print(times[0].get_text())
    timestring = times[0].get_text()
    
    if timestring.find("시간 전") != -1 or timestring.find("분 전") != -1:
        titles = ar.select('li > div > div > a')
        print(titles[0].get_text())
        print(titles[0]["href"])
   
        requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": titles[0].get_text()})

        requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": titles[0]["href"]})

