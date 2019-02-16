
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument('headless')

# executable_path = 'chromedrive.path'
# chrome_options = option
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

timeout = 5
search_content = WebDriverWait(driver, timeout).until(
    lambda d:d.find_element_by_id('kw')
)
search_content.send_keys('hello world')
button = driver.find_element_by_id('su')
button.click()
search_results = WebDriverWait(driver, timeout).until(
    lambda d:d.find_elements_by_tag_name('h3')
)
for item in search_results:
    print(item.text)

driver.close()