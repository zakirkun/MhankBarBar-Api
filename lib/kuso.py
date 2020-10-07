from requests import get
from bs4 import BeautifulSoup as bs
import json
def kuso(url):
	try:
		kuso = bs(get(url).text, 'html.parser')
		title = kuso.find('h1', class_='jdlz').text
		view = kuso.find('span', class_='viewoy').text.strip()
		info = '\n'.join(str(i.text) for i in kuso.find('div', class_='info').findAll('p'))
		sinop = kuso.findAll('div')[2].find('strong').findAllNext('p')
		sis = ''.join(sinop[1].text+sinop[3].text)
		thumb = json.loads(kuso.findAll('script')[5].string)['image']['url']
		if 'BD' in title:title = title.split('BD')[0]
		if 'Batch' in title:title = title.split('Batch')[0]
		return {
			'thumb': thumb,
			'info': info,
			'sinopsis': sis,
			'title': title
		}
	except Exception as e:return(f'Error : {e}\nAnime tidak ditemukan')