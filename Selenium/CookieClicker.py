from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'D:/Desktop/Selenium/chromedriver.exe'
url = 'https://orteil.dashnet.org/cookieclicker/'

driver = webdriver.Chrome(PATH)
driver.get(url)

driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
cookie_num = driver.find_element_by_id('cookies')
upgrades = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)]
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
	actions.perform()
	count = cookie_num.text.split()[0]
	if ',' not in count:
		count = cookie_num.text.split()[0]
	else:
		count = count.split(',')
		count = ''.join(count)
	for item in upgrades:
		if ',' in str(item):
			value = int(''.join(item.text.split(',')))
		else:
			value = int(item.text)
		if int(count) >= value:
			upgrade_it = ActionChains(driver)
			upgrade_it.move_to_element(item)
			upgrade_it.click()
			upgrade_it.perform()