import googlesearch
import re
import requests
from bs4 import BeautifulSoup

search_string = input("Enter the search string:")
results = list(googlesearch.search(search_string, num_results=30))

# Create an empty list to store the extracted emails
emails = []
print(f'{len(results)} websites found')

def get_emails(url):
    """Function that gets emails from a webpage and it's links"""
    try:
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        find_emails = soup.body.findAll(text=re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+'))
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
            emails.append(f"{email},{domain},{first_name},{last_name}\n")

            # Get all links from the website
            for a in soup.find_all("a", href=True):
                if not re.search("^(http|www)", a["href"]):
                    new_link = link + a["href"]
                    print(f'Searching for emails on {new_link}')
                    get_emails(new_link)
    except:
        pass

for i, link in enumerate(results):
    print(f'Searching for emails on {link}')
    get_emails(link)

# Save the extracted emails to a file
with open("emails.list", "w") as file:
    file.writelines(emails)

print(f'{len(emails)} email(s) saved to emails.list')

