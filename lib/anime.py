from requests import get
from bs4 import BeautifulSoup as bs
import json
def scrap_kusonime(url):
    try:
        kuso = bs(get(url).text, 'html.parser')
        title = kuso.find('h1', class_='jdlz').text
        view = kuso.find('span', class_='viewoy').text.strip()
        info = '\n'.join(str(i.text) for i in kuso.find('div', class_='info').findAll('p'))
        sinopsis = '\n'.join(str(kya.text.split('Credit')[0].split('Download')[0].strip()) for kya in kuso.findAll('p')[10:][:5]).rstrip('\n')
        smokedl = kuso.find('div', class_='smokeddl')
        ttl = len(kuso.findAll('div', class_='smokeurl'))
        tmpt_dl = list(u.text for u in smokedl.findAll('a'))
        reso = list(e.text for e in smokedl.findAll('strong'))
        link_dl = list(ntapz['href'] for ntapz in smokedl.findAll('a'))
        result_dl = ''.join(f'{tmpt_dl[o]} ({reso[o]}) => {link_dl[o]}\n\n' for o in range(len(reso)))
        thumb = json.loads(kuso.findAll('script')[5].string)['image']['url']
        if 'BD' in title:title = title.split('BD')[0].strip()
        if 'Batch' in title:title = title.split('Batch')[0].strip()
        return {
            'thumb': thumb,
            'info': info,
            'sinopsis': sinopsis,
            'title': title,
            'link_dl': result_dl
        }
    except Exception as e: return {
        'error': e,
        'msg': 'Failed get metadata!'
    }
def scrap_otakudesu(url):
    try:
        otakudesu = bs(get(url).text, 'html.parser')
        title = otakudesu.find('div', class_='jdlrx').text.split('Subtitle')[0]
        sinopsis = otakudesu.find('div', class_='sinopc').text
        info = '\n'.join(str(o.text) for o in otakudesu.find('div', class_='infozingle').findAll('p'))
        thumb = otakudesu.find('img', class_='attachment-post-thumbnail size-post-thumbnail wp-post-image')['src']
        return {
            'thumb': thumb,
            'info': info,
            'sinopsis': sinopsis,
            'title': title
        }
    except Exception as e: return {
        'error': e,
        'msg': 'Failed get metadata'
    }
