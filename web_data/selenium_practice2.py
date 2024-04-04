# 스크래핑에 필요한 라이브러리를 불러와봅시다.
from selenium import webdriver
from selenium.webdriver.common.by import By

# 예시 사이트에 요청을 진행하고, 예시 사이트의 첫 번째 이벤트의 제목을 가져와봅시다.
# driver = webdriver.Chrome()
# driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
# driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]')

# 10초동안 Implicit Wait을 진행하도록 해서 스크래핑이 잘 이루어지도록 수정해봅시다.
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    driver.implicitly_wait(10) # 렌더링이 끝나면 바로 wait 종료, 최대 10초까지만 기다림
    print(driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]').text)

# Explicit Wait를 활용해서 스크래핑이 잘 이루어지도록 코드를 작성해봅시다.
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]')))
    print(element.text)

# 10개 공연의 제목을 스크래핑하는 코드를 작성해봅시다.
with webdriver.Chrome() as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    driver.implicitly_wait(10)
    for i in range(1, 11):
        element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[{}]/div/a/div[2]/p[1]'.format(i))
        print(element.text)