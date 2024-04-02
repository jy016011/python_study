# requests 라이브러리를 불러온 후, NAVER의 홈 페이지를 요청한 후 응답 받아보기
import requests
"""
GET request
"""
res = requests.get("https://www.naver.com")
print(res)

#Header
print(res.headers)

#Body
print(res.text[:200])

"""
POST request
"""
# payload와 함께 POST를 보내봅시다 : requests.post()
payload = {"name": "Hello", "age": 13}
res = requests.post("https://webhook.site/66e120fd-f290-4be6-9af2-9b22e8bdbf02", payload)
print(res)
print(res.status_code)

"""
robots.txt
"""
res = requests.get("https://www.naver.com/robots.txt")
print(res.text)