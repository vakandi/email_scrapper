import re
import requests
from bs4 import BeautifulSoup
url = 'https://metacard.gift'
res = requests.get(url)
#soup = BeautifulSoup(res.text, 'lxml')
soup.find_all('div', {'class': "review-txt"})


def findMails(soup):
    data = ''
    for tag in soup('body'):
        data += tag.text.strip()

    return re.findall(
        '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+', data)
       # '[\w\.-]+@[\w\.-]+\.\w+', data)


emails = findMails(soup)
print(emails) if len(emails) > 0 else print('Emails Not found')
