import json
import logging
import os
import time

import requests
from bs4 import BeautifulSoup

from urls import get_urls

DUMP_PATH = f'{os.getcwd()}/dump'
URLS = get_urls()

def fetch(url):
	page = requests.get(url)
	time.sleep(2)

	if page.status_code == 404:
		raise requests.HTTPError

	return BeautifulSoup(page.content, 'html.parser')

def get_by_day_article_links(url, index_soup):  # 2021-05-01, day = 01
	# https://stackoverflow.com/a/6287601
	a = index_soup.select('h3.f16.fbo > a')
	links = [a_href['href'] for a_href in a]

	assert len(links) != 0, f'Links is empty on {url}'

	return links

def get_last_page(index_soup):
	last_page = index_soup.select('div.paging > a')[-1]['href'].split('page=')[-1]
	return int(last_page)

def get_article_contents(article_soup):
	topic, title, date_published, content, tags = None, None, None, None, None

	if article_soup.select_one('h2.red.f16'):
		topic = article_soup.select_one('h2.red.f16').text

	title = article_soup.select_one('h1#arttitle').text
	date_published = article_soup.select_one('time.grey').text

	content = article_soup.select('div.side-article.txt-article > p')
	content = [p.text for p in content]
	content = list(filter(lambda p: p[:10].lower() != 'baca juga:', content))

	tags = article_soup.select('h5.tagcloud3 > a')
	tags = [a['title'] for a in tags]

	# check next page
	next_page_link, should_go = check_next_page(article_soup)

	if should_go:
		logging.info(f'going to {next_page_link}')
		recurse_content(next_page_link, content)
	
	return {
		'topic': topic,
		'title': title,
		'date_published': date_published,
		'content': content,
		'tags': tags,
	}

def check_next_page(soup):
	try:
		next_page_a = soup.select_one('a.bgblue.white.ptb5.plr10.f18')
		should_go_to_next_page = next_page_a.text.strip().lower() == 'halaman selanjutnya'
		next_page_link = next_page_a['href']
	except:
		return None, None

	return next_page_link, should_go_to_next_page

def recurse_content(url, content):  # side effects
	soup = fetch(url)

	tmp = soup.select('div.side-article.txt-article > p')
	tmp = [p.text for p in tmp]
	tmp = list(filter(lambda p: p[:10].lower() != 'baca juga:', tmp))

	content.extend(tmp)

	# check next page
	next_page_link, should_go = check_next_page(soup)

	if should_go:
		# logging.info(f'going to {next_page_link}')
		recurse_content(next_page_link, content)

def dump_json(url, page, data):
	filename = url.split('date=')[-1] + f'-{page}.json'
	dump_path = os.path.join(DUMP_PATH, filename)

	with open(f'{dump_path}.json', 'w') as f:
		json.dump(data, f, indent=4)

def process_url(article_links):
	dump = []

	for article_link in article_links:
		# logging.info(f"processing {article_link}")

		# get_article_contents calls fetch() and might break.
		try:
			article_soup = fetch(article_link)
			data = get_article_contents(article_soup) 
		except requests.HTTPError as e:
			continue

		data['link'] = article_link
		dump.append(data)

	return dump

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, filename="tribun-bs4/tribun-bs4.logs", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
	# for url in URLS:
	for url in ['https://www.tribunnews.com/index-news/news?date=2021-5-1']:
		# logging.info(f'processing: {url}')

		# process initial page
		index_soup = fetch(url)
		last_page = get_last_page(index_soup)  # OFFSET

		"""
		article_links = get_by_day_article_links(url, index_soup)

		data = process_url(article_links)
		dump_json(url, 1, data)
		"""

		# process subsequent pages
		# page = 2  # start from next page
		page = 3
		while page <= last_page:
			page_url = url + f'&page={page}'

			# logging.info(f'processing: {page_url}')
			page_soup = fetch(page_url)
			article_links = get_by_day_article_links(url, page_soup)
			
			data = process_url(article_links)
			dump_json(page_url, page, data)

			page += 1
		
