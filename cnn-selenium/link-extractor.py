import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from dates_parameter import return_date_params

DUMP_PATH = 'dump/cnn/link'

def dump_links(article_links, date_params, dump_path=DUMP_PATH):
	dump_file = os.path.join(DUMP_PATH, date_params)

	with open(f'{dump_file}.link', 'w') as f:
		f.writelines('\n'.join(article_links))

def run_driver(dates):
	month = int(dates.split('/')[0])
	day = int(dates.split('/')[1])
	date_params = f'2021{dates}'.replace('/', '')

	URL = 'https://www.cnnindonesia.com/indeks'

	# https://stackoverflow.com/a/55834112/8996974
	options = FirefoxOptions()
	options.add_argument("--headless")
	driver = webdriver.Firefox(options=options)
	driver.get(URL)

	# Element obscured; I haven't solved this, but this SO link might help
	# (maybe next time the error came up)
	# https://stackoverflow.com/a/49939793
	driver.implicitly_wait(5)

	# Wait until
	# https://stackoverflow.com/a/65142989/8996974
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='date1']"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='datepick-month-header']/select[@title='Change the month']/option[@value='{month}/2021']"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='datepick-month']/table/tbody//a[text()='{day}']"))).click()

	for _ in range(100):  # while True, actually (assume: page won't reach 100)
		driver.implicitly_wait(5)

		try:
			next_button = driver.find_element_by_class_name('btn.btn__more')
		except:
			break
		
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn__more"))).click()

	articles = driver.find_elements_by_xpath(f"//a[contains(@href, {date_params})]")
	article_links = [article.get_attribute('href') for article in articles]
	
	dump_links(article_links, date_params)

	driver.close()

if __name__ == '__main__':
	"""
	date_params = return_date_params()

	for date_param in date_params:
		run_driver(date_param)
		print(f'Done processing {date_param}')
		time.sleep(3)
	"""

	run_driver('05/03')
	print('Done')
