# for dynamic web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for visualization
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# for count word frequency
from collections import Counter

# for delay after get request in loop
import time


def switch_to_iframe(driver, id):
    iframe = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))
    driver.switch_to.frame(iframe)


def scroll_down_to_end(driver):
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    for i in range(10):
        body.send_keys(Keys.PAGE_DOWN)

def main():
    url = "https://search.naver.com/search.naver?where=news&query=%EB%89%B4%EC%8A%A4&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0"
    font_path = "/Users/junyoung-kim/devcourse/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf"
    driver = webdriver.Chrome()
    driver.get(url)
    # scroll_down_to_end(driver)
    # time.sleep(1)
    # scroll_down_to_end(driver)
    # time.sleep(1)
    # scroll_down_to_end(driver)
    # time.sleep(30)
    news_list_block = (
        WebDriverWait(driver, 5)
        .until(EC.presence_of_element_located((By.CLASS_NAME, "list_news._infinite_list")))
    )
    news_list = news_list_block.find_elements(By.TAG_NAME, "li")
    time.sleep(2)
    for news in news_list:
        # news_contents = news.find_element(By.CLASS_NAME, "news_contents")
        title = news.find_element(By.CLASS_NAME, "news_tit")
        print(title.get_attribute('title'))


if __name__ == "__main__":
    main()
