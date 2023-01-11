import re
import requests
from bs4 import BeautifulSoup
import sys

def search_emails():
    sent_emails = []
    link_extensions = ['', 'contact', 'contact-us', 'contact.html', 'contact-us.html']
    # Get the search string from the command line argument
    search_string = sys.argv[1].replace(' ', '+')
    url = f"https://www.google.com/search?q={search_string}&num=100"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.r a')
    links = [link.get('href') for link in links]
    links = [link for link in links if '/url?q=' in link]
    links = [link.replace('/url?q=', '') for link in links]
    pattern = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}')
    print(f"Search_pail function done... adding infos to emails.list")

    with open('emails.list', 'w') as f:
        for link in links:
            try:
                for extension in link_extensions:
                    print(f"Beginning of the informations adding")
                    source = requests.get(link + extension, timeout=10)
                    soup = BeautifulSoup(source.text, 'lxml')
                    emails = pattern.findall(str(soup))
                    for email in set(emails):
                        if email not in sent_emails:
                            domain = link.split("//")[-1].split("/")[0]
                            f.write(email + ' ' + domain + '\n')
                            sent_emails.append(email)
            except:
                pass
    print(f"{len(sent_emails)} unique emails were found and saved to 'emails.list'")
    print(res.status_code)
    print(res.headers)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_emails()
    else:
        print("Provide a search string as an argument")

