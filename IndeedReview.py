import requests
from bs4 import BeautifulSoup

web = input("Please enter indeed review url: ")
res = requests.get(web)
soup = BeautifulSoup(res.text, 'lxml')
for item in soup.find_all(class_='css-82l4gy eu4oa1w0'):
    print(item.text)
