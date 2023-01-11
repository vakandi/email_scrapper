import re
import requests
from bs4 import BeautifulSoup

def search_emails(search_string):
    sent_emails = []
    link_extensions = ['', 'contact', 'contact-us', 'contact.html', 'contact-us.html']
    # Google search
    search_string = search_string.replace(' ', '+')
    url = f"https://www.google.com/search?q={search_string}&num=100"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.r a')
    links = [link.get('href') for link in links]
    links = [link for link in links if '/url?q=' in link]
    links = [link.replace('/url?q=', '') for link in links]

    def check_email(emails):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        for email in emails:
            if(re.search(regex,email) or re.search(regex2, email)):
                if email not in sent_emails:
                    sent_emails.append(email)
                return True
                break
            else:
                if len(email) <= 195:
                    print("Invalid Email")
                    print("\t" + email)
                else:
                    pass
    for link in links:
        try:
            for extension in link_extensions:
                source = requests.get(link + extension, timeout=10)
                soup = BeautifulSoup(source.text, 'lxml')
                print("Looking for emails in " + link + extension)
                find_emails = soup.body.findAll(text=re.compile('@'))
                check_email(find_emails)
                if check_email(find_emails):
                    break
        except:
            pass
    print("Scraping finished, Sent emails: ", sent_emails)

