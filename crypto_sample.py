import requests
from bs4 import BeautifulSoup

import schedule
import time

def searchKeyword1():
    postSlackMessage("암호화폐")


def postSlackMessage(keyword):
    token = "{token}"
    channel = "#news_monitoring"

    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+ keyword + "&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0",
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
    
            response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": titles[0].get_text()})
            #print("response" + response.status_code)

            response2= requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": titles[0]["href"]})
            #print("response2" + response2.status_code)


schedule.every().day.at("14:16").do(searchKeyword1)

while True:
    schedule.run_pending()
    time.sleep(1)