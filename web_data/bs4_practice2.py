# 스크래핑에 필요한 라이브러리를 불러와봅시다.
import requests
from bs4 import BeautifulSoup as bs

# 예시 사이트에 요청을 진행하고, 응답을 바탕으로 BeautifulSoup 객체를 만들어봅시다.
res = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
soup = bs(res.text, "html.parser")

# <h3> 태그에 해당하는 요소를 하나 찾아봅시다
book = soup.find("h3")

# <h3> 태그에 해당하는 요소를 모두 찾아봅시다
h3_results = soup.find_all("h3")
print(len(h3_results))


# <h3> 태그에 해당하는 요소를 하나 찾아봅시다
book = soup.find("h3")
print(book.a.text)

for book in h3_results:
    print(book.a.text)

for book in h3_results:
    print(book.a["title"])
