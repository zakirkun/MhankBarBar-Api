from requests import get
from bs4 import BeautifulSoup as bs

def scrap_komiku(url):
    try:
        ko = bs(get(url).text, 'html.parser')
        thumb = ko.find('div', class_='ims').img['src']
        info_ = ko.find('table', class_='inftable').findAll('td')
        info = ''
        for i in range(len(info_)):
            if i == 0: info += f'{info_[i].text} : {info_[i+1].text}\n'
            elif i % 2 == 0 and info_[i].text not in info: info += f'{info_[i].text} : '
            elif i % 2 != 0 and info_[i].text not in info: info += f'{info_[i].text}\n'
        genre = 'Genre : '
        genre += ''.join(f'{i.text},' for i in ko.find('ul', class_='genre').contents).strip(',')
        sinopsis = ko.find('section', id='Sinopsis').ul.text
        jdllink = [i.text.replace('\n\n','').rstrip('\n').rstrip('\t').rstrip('\n')+'\n' for i in ko.findAll('td', class_='judulseries')]
        dllink = ['https://komiku.co.id'+i.a['href'] for i in ko.findAll('td', class_='tanggalseries dl')]
        result_dl = ''.join(f'{jdllink[i]} => {dllink[i]}\n' for i in range(len(dllink)))
        return {
            'info': info,
            'genre': genre,
            'thumb': thumb,
            'sinopsis': sinopsis,
            'dl_link': result_dl
        }
    except Exception as e:
        return {
            'error': e,
            'msg': 'Failed get metadata'
        }

def search_komiku(query):
    try:
        url = bs(get('https://komiku.co.id/?post_type=manga&s=%s' % query).text, 'html.parser').find('div', class_='bge').a['href']
        return url
    except:
        return ('Manga %s Tidak di temukan!' % query)
