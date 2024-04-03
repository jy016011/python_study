# www.example.com 사이트를 요청한 후 응답 받아보기
import requests
# BeautifulSoup4 - bs4를 불러와봅시다.
from bs4 import BeautifulSoup

res = requests.get("http://www.example.com")

# BeautifulSoup객체를 만들어봅시다.
# 첫번째 인자로는 response의 body를 텍스트로 전달합니다.
# 두번째 인자로는 "html"로 분석한다는 것을 명시해줍니다.
soup = BeautifulSoup(res.text, "html.parser")

# 객체 soup의 .prettify()를 활용하면 분석된 HTML을 보기 편하게 반환해줍니다.

print(soup.prettify())

# title 가져오기
print(soup.title)


# head 가져오기
print(soup.head)

# body 가져오기
print(soup.body)


# <h1> 태그로 감싸진 요소 하나 찾기
h1 = soup.find("h1")

# <p> 태그로 감싸진 요소들 찾기
print(soup.find_all("p"))

# 태그 이름 가져오기
print(h1.name)


# 태그 내용 가져오기
print(h1.text)