import requests, re
from urllib.parse import quote
from bs4 import BeautifulSoup
def gsearch(query):
    src = requests.get("https://www.google.com/search?q="+quote(query)).text
    return re.findall('<a href="/url\?q\=(.*?)\&amp;',src)
def brainly(url):
    print(url)
    bs=BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}).text, html.parser)
    Tangg=bs.find_all('span',class_='sg-text sg-text--xsmall sg-text--gray-secondary')[0]('time')[0]['title']
    angkatan=bs.find_all('span',itemprop='name',class_='sg-text sg-text--xsmall sg-text--gray-secondary sg-text--link')[1].text
    mapel=bs.find_all('span',itemprop='name',class_='sg-text sg-text--xsmall sg-text--gray-secondary sg-text--link')[0].text
    answer=[]
    pertanyaan=bs.find_all('span',class_='sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary')[0].text
    for jawaban in bs.find_all('div',class_='sg-text sg-text--break-words brn-rich-content js-answer-content'):
        answer.append(jawaban.text)
    return {
        'soal':pertanyaan,
        'angkatan':angkatan,
        'mapel':mapel,
        'tanggal':Tangg,
        'jawaban':answer
        }
