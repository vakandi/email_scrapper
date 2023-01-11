import googlesearch
import re
import requests
from bs4 import BeautifulSoup
search_string = input("Enter the search string:")
results = list(googlesearch.search(search_string, num_results=2))

import os

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'emails.list')

print(f'{len(results)} websites found')

email_count = 0

def findMails(soup):
    data = ''
    for tag in soup('body'):
        data += tag.text.strip()

    return re.findall(
        '[\w\.-]+@[\w\.-]+\.\w+', data)



def get_emails(url):
    """Function that gets emails from a webpage and it's links"""
    global email_count
    try:
#        source = requests.get(url)
#        soup = BeautifulSoup(source.text, 'lxml')
#        find_emails = soup.find_all(text=re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+'))
        soup = BeautifulSoup(source.text, 'html.parser')
        email = findMails(soup)
        print(email) if len(email) > 0 else print('Emails Not found')

        nb_email_found = len(email)
        email_count += nb_email_found
        print(f'{nb_email_found} email(s) found on {url}')
        for email in find_emails:
            print(email)
            email_name = email.split("@")[0]
            first_name = last_name = None
            if '.' in email_name:
               first_name,last_name = email_name.split('.')
            else:
                first_name = email_name
            domain = re.search("@[\w.]+", email).group()[1:]
            try:
                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(f"{email},{domain},{first_name},{last_name}\n")
                    print(f"{email} saved to emails.list")
            except OSError:
                print(f"Cannot write to {file_path}. Do you have permission to create files in this directory?")
            #Collect links
            for a in soup.find_all("a", href=True):
                if not re.search("^(http|www)", a["href"]):
                    new_link = url + a["href"]
                    print(f'Searching for emails on {new_link}')
                    try:
                        get_emails(new_link)
                    except requests.exceptions.RequestException as e:
                        print(f"Couldn't connect to {new_link}. Error: {e}")
    except:
        pass

for i, link in enumerate(results):
    print(f'Searching for emails on {link}')
    try:
        get_emails(link)
    except requests.exceptions.RequestException as e:
        print(f"Couldn't connect to {link}. Error: {e}")
print(f'{email_count} email(s) found in total')

