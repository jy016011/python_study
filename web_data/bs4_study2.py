import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://library.gabia.com/")
soup = bs(page.text, "lxml")

# esg-entry-content 클래스로 설정된 div태그들의 하위에 존재하는 a태그의 하위에 존재하는 span태그 모두 가져오기
elements = soup.select('div.esg-entry-content a > span')
print(elements)

# 각 게시글 제목 불러오기
for index, element in enumerate(elements, start=1):
    # element.text: element의 콘텐츠(태그 사이에 있는 텍스트) 불러오기
    print("{} 번째 게시글의 제목: {}".format(index, element.text))

# esg-entry-content 클래스로 설정된 div태그들의 하위 태그 중, eg-grant-element-0 클래스를 갖는 a태그만 추출
elements2 = soup.select('div.esg-entry-content a.eg-grant-element-0')
print(elements2)

for index, element in enumerate(elements2, start=1):
    print(element.attrs) # element의 속성 가져오기{딕셔너리 형태, key(속성) : value(속성 값)}
    # element.attrs['href']: element의 속성 중 href 속성 값 가져오기
    print("{} 번째 게시글: {}, {}".format(index, element.text, element.attrs['href']))
titles = []
links = []
for element in elements2:
    titles.append(element.text)
    links.append(element.attrs['href'])

df = pd.DataFrame()
df['titles'] = titles
df['links'] = links
print(df)
# df.to_csv('./library_gabia.csv')