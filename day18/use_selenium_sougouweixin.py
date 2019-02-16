from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(chrome_options=option)
url = 'https://weixin.sogou.com/weixin?query=python_shequ'
timeout = 5
url_base = 'https://mp.weixin.qq.com'
driver.get(url)
link = WebDriverWait(driver, timeout).until(
    lambda d:d.find_element_by_link_text('Python爱好者社区')
)
link.click()
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
article_links = WebDriverWait(driver, timeout).until(
    lambda d:d.find_elements_by_class_name('weui_media_title')
)
# print(article_links)
for item in article_links:
    href = url_base + item.get_attribute('hrefs')
    print(href)

driver.close()