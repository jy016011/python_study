from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

query = input('검색할 지역과 키워드를 입력하세요: ')
url = "https://map.naver.com/p"
driver = webdriver.Chrome()
time.sleep(3)
driver.get(url)
time.sleep(3)

input_box = driver.find_element(By.CLASS_NAME, "input_search")
input_box.send_keys(query)
input_box.send_keys(Keys.RETURN)
time.sleep(5)
# (ActionChains(driver).send_keys_to_element(input_box, query)
#  .send_keys_to_element(input_box, Keys.RETURN).perform())

iframe = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "searchIframe")))
driver.switch_to.frame(iframe)
time.sleep(3)
for i in range(1, 11):
    element = driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[{}]'.format(i))
    spans = element.find_elements(By.TAG_NAME, 'span')
    if i < 3:
        print(spans[1].text)
        continue
    print(spans[0].text)

driver.switch_to.default_content()
time.sleep(3)
