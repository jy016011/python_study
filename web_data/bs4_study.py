import requests
from bs4 import BeautifulSoup
url = 'https://example.com/'
response = requests.get(url)
print(response.status_code)

# using html.parser
soup = BeautifulSoup(response.content, 'html.parser')
headers = soup.find_all('h1')
print(headers)

# using lxml, faster than html.parser
html = response.text
soup = BeautifulSoup(html, 'lxml')

# find all tags wanted
p_tags = soup.select('p')
print(p_tags)
print(p_tags[1])

print()
p_tags = soup.find_all('p')
print(p_tags)
print(p_tags[1])
