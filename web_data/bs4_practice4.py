# 필요한 라이브러리를 불러온 후, 요청을 진행해봅시다.
import requests
from bs4 import BeautifulSoup as bs
import time

# 다음 User-Agent를 추가해봅시다.
user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

res = requests.get("https://hashcode.co.kr/", user_agent) #param: url, header
print(res.text)

# 응답을 바탕으로 BeautifulSoup 객체를 생성해봅시다.
soup = bs(res.text, "html.parser")

# 질문의 빈도를 체크하는 dict를 만든 후, 빈도를 체크해봅시다.

questions = soup.find_all("li", "question-list-item")

for question in questions:
    print(question.find("div", "question").find("div", "top").h4.text)

# Pagination이 되어있는 질문 리스트의 제목을 모두 가져와봅시다.
# 과도한 요청을 방지하기 위해 1초마다 요청을 보내봅시다.

for i in range(1, 6):
    res = requests.get("https://hashcode.co.kr/?page={}".format(i), user_agent)
    soup = bs(res.text, "html.parser")
    print("{}번째 페이지".format(i))
    questions = soup.find_all("li", "question-list-item")
    for question in questions:
        print(question.find("div", "question").find("div", "top").h4.text)
    print("\n\n")
    time.sleep(0.5)

