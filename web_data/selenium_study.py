# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# HTML Locator import
from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행
driver = webdriver.Chrome()

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.google.co.kr/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)

# 검색어 창 가져오기
search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
# search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

# 검색어 창에 "파이썬" 입력하기
search_box.send_keys('파이썬')

# 검색어창 엔터 누르기
search_box.send_keys(Keys.RETURN)
time.sleep(5)