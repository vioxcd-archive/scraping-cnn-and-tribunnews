import json
import logging
import os
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

CNN_ROOT = 'dump/cnn'

def load_files(root=CNN_ROOT):
	link_path = os.path.join(root, 'link')
	files = os.listdir(link_path)

	if len(files) == 0:
		raise FileNotFoundError(f'check your {root} folder, ensure link files exist')

	files = [os.path.join(CNN_ROOT, file_) for file_ in files]
	return files

def load_links(file_):
	links = []

	with open(file_, 'r') as f:
		tmp = f.readlines()
		tmp = list(map(str.strip, tmp))
		links.extend(tmp)

	return links

def fetch(url):
	page = requests.get(url)
	time.sleep(.5)

	if page.status_code == 404:
		raise requests.HTTPError

	return BeautifulSoup(page.content, 'html.parser')

def process_page(soup):
	"""return title, date, content, related topics"""
	title = soup.find('h1', class_='title').text.strip()
	date = soup.find('div', class_='date').text.split('| ')[-1].strip()
	content = soup.find('div', class_='detail_text')
	ps = content.find_all('p')
	ps = [p.text for p in ps]

	# might be None?
	related_topic = soup.find('div', class_='list-topik-terkait').attrs.get('name')
	if related_topic:
		related_topic = related_topic.split('|')

	return {
		'title': title,
		'date': date,
		'content': ps,
		'related_topic': related_topic,
	}

def dump(filename, data, root=CNN_ROOT):
	"""data are for a day (one .link file)"""
	dump_path = os.path.join(root, 'articles', filename)

	with open(f'{dump_path}.json', 'w') as f:
		json.dump(data, f, indent=4)
	
	print(f'Dumped {dump_path}')

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, filename="cnn-selenium/page-process.logs", filemode="w",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

	# files = load_files()
	files = [
		f'{CNN_ROOT}/link/20210502.link'
	]

	for file_ in files:
		logging.info(f'Processing {file_}')

		links = load_links(file_)
		data = []

		for link in tqdm(links):
			logging.info(f'Processing {link}')
			
			soup = fetch(link)

			"""Content error comes from page where the content is not text, but videos or photos"""
			try:
				page_data = process_page(soup)
				page_data['link'] = link
				data.append(page_data)
			except Exception as e:
				logging.error(f'Error found: {e}')

		filename = file_.split('/')[-1].split('.')[0]  # [root, link folder, (filename, .link format)]
		dump(filename, data)

		time.sleep(3)
