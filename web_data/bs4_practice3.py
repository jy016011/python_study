# 스크래핑에 필요한 라이브러리를 불러와봅시다.
import requests
from bs4 import BeautifulSoup as bs

## 또 다른 연습 사이트를 이용해봅시다.
res = requests.get("https://programmers.co.kr/pages/data_engineering")
soup = bs(res.text, "html.parser")

## id 없이 div 태그를 찾아봅시다.
print(soup.find("div"))

## id가 results인 div 태그를 찾아봅시다.
id_result = soup.find("div", id="results")
print(id_result)

# class가 "page-header"인 div 태그를 찾아봅시다.
class_result = soup.find("div", "page-header")
print(class_result)

# 위 결과에서 text 값을 깔끔하게 가져와봅시다.
print(class_result.h1.text.strip())