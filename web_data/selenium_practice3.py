# driver를 이용해 해당 사이트에 요청을 보내봅시다.
# 스크래핑에 필요한 라이브러리를 불러와봅시다.
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://hashcode.co.kr/')

# 내비게이션 바에서 "로그인" 버튼을 찾아 눌러봅시다.
button = driver.find_element(By.XPATH, '//*[@id="main-app-header"]/header/section/div/div/div/a[1]')
ActionChains(driver).click(button).perform()
time.sleep(1)

# "아이디" input 요소에 여러분의 아이디를 입력합니다.
id_input = driver.find_element(By.NAME, "email")
ActionChains(driver).send_keys_to_element(id_input, "id").perform()
time.sleep(1)

# "패스워드" input 요소에 여러분의 비밀번호를 입력합니다.
pw_input = driver.find_element(By.XPATH, '//*[@id="main-app-account"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[4]/input')
ActionChains(driver).send_keys_to_element(pw_input, "password").perform()
time.sleep(1)

# "로그인" 버튼을 눌러서 로그인을 완료합니다.
button_sign_in = driver.find_element(By.XPATH, '//*[@id="main-app-account"]/div/div[2]/div/div[2]/div[1]/div/div[2]/button')
ActionChains(driver).click(button_sign_in).perform()
time.sleep(1)