import janome
import requests
from janome.tokenizer import Tokenizer
from bs4 import BeautifulSoup

def main():

    t = Tokenizer()

    for token in t.tokenize(u'pythonの本を読みました。とてもおもしろい本でした'):
        print(token)


    url = 'https://play.google.com/store/apps/details?id=jp.co.nikko_data.japantaxi'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    for sponsor in sponsors:
        url = sponsor.h3.a['href']
        name = sponsor.h4.text
        print(name, url)
