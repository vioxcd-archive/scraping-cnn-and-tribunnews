from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.cnnindonesia.com/indeks'

driver = webdriver.Firefox()
driver.get(URL)

# https://stackoverflow.com/a/65142989/8996974
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='date1']"))).click()
print('interacted with datepicker')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='datepick-month-header']/select[@title='Change the month']/option[@value='5/2021']"))).click()
print('interacted with monthpicker')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='datepick-month']/table/tbody//a[text()='1']"))).click()
print('interacted with daypicker')

driver.implicitly_wait(5)
articles = driver.find_elements_by_xpath("//a[contains(@href, '20210501')]")

for article in articles:
	print(article.get_attribute('href'))

driver.close()
