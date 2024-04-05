# 다음 User-Agent를 추가해봅시다.

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

# Pagination이 되어있는 질문 리스트의 제목을 모두 가져와 리스트 questions에 저장해봅시다.
# https://hashcode.co.kr/?page={i}
# 과도한 요청을 방지하기 위해 0.5초마다 요청을 보내봅시다.
import requests
import time
from bs4 import BeautifulSoup as bs

questions = []

for i in range(1, 6):
    res = requests.get("https://hashcode.co.kr/?page={}".format(i), user_agent)
    soup = bs(res.text, "html.parser")
    parsed_datas = soup.find_all("li", "question-list-item")
    for data in parsed_datas:
        questions.append(data.h4.text.strip())
    time.sleep(0.5)

# 텍스트 구름을 그리기 위해 필요한 라이브러리를 불러와봅시다.

# 시각화에 쓰이는 라이브러리
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 횟수를 기반으로 딕셔너리 생성
from collections import Counter

# 문장에서 명사를 추출하는 형태소 분석 라이브러리
from konlpy.tag import Hannanum
# Hannanum 객체를 생성한 후, .nouns()를 통해 명사를 추출합니다.
words = []
hannanum = Hannanum()
for question in questions:
    nouns = hannanum.nouns(question)
    words += nouns

# counter를 이용해 각 단어의 개수를 세줍니다.
counter = Counter(words)

# WordCloud를 이용해 텍스트 구름을 만들어봅시다.
wordcloud = WordCloud(
    font_path = "/Users/junyoung-kim/devcourse/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf",
    background_color = "white",
    width=1000,
    height=1000,
)

img = wordcloud.generate_from_frequencies(counter)

plt.imshow(img)
plt.show()