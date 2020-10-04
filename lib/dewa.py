from requests import get
from urllib.parse import *
from bs4 import BeautifulSoup as bs
def cari(url):
	try:
		bes=bs(get(url).text, 'html.parser')
		scrap=bes.findAll('span')
		info = '%s\nRating: %s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (scrap[6].text,scrap[4].text.strip(),scrap[7].text,scrap[8].text,scrap[9].text,scrap[10].text,scrap[11].text,scrap[12].text,scrap[13].text,scrap[14].text,scrap[16].text)
		desc=bes.find('div', {'itemprop':'description'}).contents[3].text.replace('& quot;','&').replace('& Quot;','&').replace('& mdash;','&')
		hasil='Sinopsis : %s' % desc
		return {
			'cover':bes.find_all('div',itemprop='image')[0].find_all('img',itemprop='image')[0]['src'],
			'thumb':str(bes.find('div', class_="_2S7A1")).split('url(')[1].strip(')"></div>'),
			'result':hasil,
			'info':info
		}
	except Exception as e:return(f'Error : {e}\n\nanime tidak di temukan')
