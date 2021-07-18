from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = 'D:/Desktop/Selenium/chromedriver.exe'
url = 'https://www.google.com/'
driver = webdriver.Chrome(PATH)

driver.get(url)
print(driver.title)
name = 'q'
search = driver.find_element_by_name(name)
search.send_keys('Hello, World!')
search.send_keys(Keys.RETURN)