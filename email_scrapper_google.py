from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from bs4 import BeautifulSoup
import ssl
import requests

sent_emails = []

link_extensions = ['', 'contact', 'contact-us', 'contact.html', 'contact-us.html']

def check_email(emails):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' #"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+"
    for email in emails:
        # Check if the text is an email address
        if(re.search(regex,email) or re.search(regex2, email)):
            print("Valid Email")
            print("\t" + email)
            if email not in sent_emails:
                sent_emails.append(email)
            print(sent_emails)
            return True
            break
        else:
            print("Invalid Email")
            if len(email) <= 195:
                print("\t" + email)
            else:
                pass

def validurl(link):
    # Check the validity of the URL. In this case, we only want to scrape the homepages of websites.
    pattern = "(https://|http://)+(|www.)+[a-zA-Z0-9.-]+.(com|net|co|org|us|info|biz|me)+(|/)"
    p = re.compile(pattern)
    if(re.fullmatch(p, link)):
            for extension in link_extensions:
                try:
                    source = requests.get(link + extension, timeout=10)
                    soup = BeautifulSoup(source.text, 'lxml')
                    print("Looking for emails in " + link + extension)
                    # Look for emails on the website
                    find_emails = soup.body.findAll(text=re.compile('@'))
                    check_email(find_emails)
                    if check_email(find_emails):
                        break
                except:
                    pass

