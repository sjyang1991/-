# 관심 채용정보 크롤링 및 새 게시물 텔레그램 알림 예제
import requests
from bs4 import BeautifulSoup
from config import CRAWLING_URL
from telegram_send import send

#크롤링
params = {
    'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site' : 'none',
    'Sec-Fetch-Mode' : 'navigate',
    'Sec-Fetch-User' : '?1',
    'Sec-Fetch-Dest' : 'document',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie' : 'stel_ssid=db397034404ae932a2_6395906157645138433; _ga=GA1.2.1402317097.1587653246; _gid=GA1.2.1671355373.1587653246'
}
response = requests.get(CRAWLING_URL, params)
html = response.text
soup = BeautifulSoup(html, "html.parser")
hotKeys = soup.select(".tgme_widget_message_text")

for row in hotKeys:
    #print(row.text)
    if row.text.find('!@#') != -1:
    #    print(row.text.find('!@#'))
        print(row.text)
        send(row.text)


