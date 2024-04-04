# selenium으로부터 webdriver 모듈을 불러옵니다.
from selenium import webdriver
from selenium.webdriver.common.by import By


# webdriver.Chrome 객체 생성
driver = webdriver.Chrome()

# http://www.example.com 으로 요청을 보내봅시다.
driver.get("http://www.example.com")

# Response의 HTML 문서 확인: page_source
driver = webdriver.Chrome()
driver.get("http://www.example.com")
print(driver.page_source)

# with-as를 사용해서 위 코드를 다시 적어봅시다.
with webdriver.Chrome() as driver:
    driver.get("http://www.example.com")
    print(driver.page_source)

# p 태그에 해당하는 요소 하나를 찾아봅시다.
with webdriver.Chrome() as driver:
    driver.get("http://www.example.com")
    print(driver.find_element(By.TAG_NAME, "p").text)


# p 태그에 해당하는 요소 여러개를 찾아봅시다.
with webdriver.Chrome() as driver:
    driver.get("http://www.example.com")
    for element in driver.find_elements(By.TAG_NAME, "p"):
        print("Text: ", element.text)