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
    for i in range(40):
        body.send_keys(Keys.PAGE_DOWN)


def get_food_categories(driver):
    categories = []
    search_results_block = (
        WebDriverWait(driver, 5)
        .until(EC.presence_of_element_located((By.TAG_NAME, 'ul')))
    )
    restaurants = search_results_block.find_elements(By.TAG_NAME, 'li')
    for restaurant in restaurants:
        category_element = restaurant.find_element(By.CLASS_NAME, 'KCMnt')
        categories += category_element.text.split(",")
    return categories


def get_next_page_button(driver):
    next_buttons_block = (
        WebDriverWait(driver, 5)
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'zRM9F')))
    )
    next_buttons = next_buttons_block.find_elements(By.CSS_SELECTOR, 'a')
    return next_buttons[-1]

def search(driver, query):
    input_box = (
        WebDriverWait(driver, 5)
        .until(EC.presence_of_element_located((By.CLASS_NAME, "input_search")))
    )

    input_box.send_keys(query)
    input_box.send_keys(Keys.RETURN)


def main():
    query = input('검색할 지역을 입력하세요: ') + " 맛집"
    url = "https://map.naver.com/p"
    font_path = "/Users/junyoung-kim/devcourse/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf"
    driver = webdriver.Chrome()
    print("{}의 카테고리를 수집합니다".format(query))
    driver.get(url)

    search(driver, query)

    switch_to_iframe(driver, "searchIframe")
    categories = []

    while True:
        scroll_down_to_end(driver)
        categories += get_food_categories(driver)
        next_button = get_next_page_button(driver)
        if next_button.get_attribute('aria-disabled') == 'true':
            break
        next_button.click()
        time.sleep(1)

    category_counter = Counter(categories)
    print(category_counter)
    food_category_cloud = WordCloud(
        font_path=font_path,
        background_color="white",
        height=1000,
        width=1000,
    )

    food_category_cloud_img = food_category_cloud.generate_from_frequencies(category_counter)
    plt.imshow(food_category_cloud_img)
    plt.show()


if __name__ == "__main__":
    main()
