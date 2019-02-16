from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome()
url = 'https://www.toutiao.com/'
timeout = 5
driver.get(url)

links = WebDriverWait(driver, timeout).until(
    lambda d:d.find_elements_by_class_name('link')
)
for item in links:
    print(item.text)
    print(item.get_attribute('href'))

driver.close()