# 텍스트 구름을 그리기 위해 필요한 라이브러리를 불러와봅시다.

# 시각화에 쓰이는 라이브러리
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 횟수를 기반으로 딕셔너리 생성
from collections import Counter

# 문장에서 명사를 추출하는 형태소 분석 라이브러리
from konlpy.tag import Hannanum

# 워드클라우드를 만드는 데 사용할 애국가 가사입니다.

national_anthem = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
남산 위에 저 소나무 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
이 기상과 이 맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
"""

# Hannanum 객체를 생성한 후, .nouns()를 통해 명사를 추출합니다.

hannanum = Hannanum()
nouns = hannanum.nouns(national_anthem)
words = [noun for noun in nouns if len(noun) > 1]

# counter를 이용해 각 단어의 개수를 세줍니다.

counter = Counter(words)
print(counter)

# WordCloud를 이용해 텍스트 구름을 만들어봅시다.
wordcloud = WordCloud(
    font_path="/Users/junyoung-kim/devcourse/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf",
    background_color="white",
    width=1000,
    height=1000
)

img = wordcloud.generate_from_frequencies(counter)
plt.imshow(img)
plt.show()
