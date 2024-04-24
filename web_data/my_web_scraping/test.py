import pandas as pd
import requests
# df = pd.read_csv("recruitment_infos4.csv")
# print(df)
query = "데이터엔지니어"
page_no = 1
url = f"https://www.jobkorea.co.kr/Search/?stext={query}&duty=1000236&tabType=recruit&Page_No={page_no}"
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
})
print(response.text)