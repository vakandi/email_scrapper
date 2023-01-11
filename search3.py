import googlesearch
import re
import requests
from bs4 import BeautifulSoup

search_string = input("Enter the search string:")
results = list(googlesearch.search(search_string, num_results=30))

print(f'{len(results)} websites found')

def get_emails(url):
"""Function that gets emails from a webpage and it's links"""
try:
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
find_emails = soup.body.findAll(text=re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9-.]+'))
nb_email_found = len(find_emails)
print(f'{nb_email_found} email(s) found on {url}')
for email in find_emails:
email_name = email.split("@")[0]
first_name = last_name = None
if '.' in email_name:
first_name,last_name = email_name.split('.')
else:
first_name = email_name
domain = re.search("@[\w.]+", email).group()[1:]
with open("emails.list", "a", encoding="utf-8") as file:
file.write(f"{email},{domain},{first_name},{last_name}\n")
print(f"{email} saved to emails.list")
                for a in soup.find_all("a", href=True):
                    if not re.search("^(http|www)", a["href"]):
                        new_link = url + a["href"]
                        print(f'Searching for emails on {new_link}')
                        get_emails(new_link)
email_count = 0
for i, link in enumerate(results):
print(f'Searching for emails on {link}')
email_count += get_emails(link)
print(f'{email_count} email(s) found')

print("Finish")
