import googlesearch
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

search_string = input("Enter the search string:")
results = list(googlesearch.search(search_string, num_results=50))

import os

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'emails.list')

print(f'{len(results)} websites found')

email_count = 0


visited_pages = set()
def get_emails(url):
    """Function that gets emails from a webpage and it's links"""
    global email_count, visited_pages
    start_time = time.time()
    try:
        source = requests.get(url, timeout=5) # set timeout to 5 seconds
        if url in visited_pages:
            return
        visited_pages.add(url)
        try:
            source = requests.get(url)
            soup = BeautifulSoup(source.text, 'lxml')
            find_emails = soup.find_all(text=re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+'))
            nb_email_found = len(find_emails)
            email_count += nb_email_found
            print(f'{nb_email_found} email(s) found on {url}')
            for email in find_emails:
                email_name = email.split("@")[0]
                first_name, last_name = email_name.split('.') if '.' in email_name else (email_name, None)
                domain = re.search("@[\w.]+", email).group()[1:]
                try:
                    with open(file_path, "a", encoding="utf-8") as file:
                        file.write(f"{email},{domain},{first_name},{last_name}\n")
                        print(f"{email} saved to emails.list")
                except OSError:
                    print(f"Cannot write to {file_path}. Do you have permission to create files in this directory?")
                for a in soup.find_all("a", href=True):
                    if is_valid_url(a["href"]) and not re.search("^(http|www)", a["href"]):
                        new_link = url + a["href"]
                        print(f'Searching for emails on {new_link}')
                    try:
                        get_emails(new_link)
                    except requests.exceptions.RequestException as e:
                        print(f"Couldn't connect to {new_link}. Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    except Exception as e:
            print(f"An error occurred: {e}")
    finally:
            end_time = time.time()
            if end_time - start_time > 5:
                print(f'{url} took more than 5 seconds to load.')


for i, link in enumerate(results):
    print(f'Searching for emails on {link}')
    try:
        get_emails(link)
    except requests.exceptions.RequestException as e:
        print(f"Couldn't connect to {link}. Error: {e}")
print(f'{email_count} email(s) found in total')
