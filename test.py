from googlesearch import search
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


choice_arg = input("[1] Simple search\n[2] Domain Search\n")

if choice_arg == "1":
    search_string = input("Enter the search string:")
    results = list(search(search_string, num_results=50))
    print("Searching... " + search_string)
elif choice_arg == "2":
    search_string = input("Enter the domain:")
    results = search(search_string, num_results=10, site_search=search_string)
    print("Domain searching... " + search_string)
else:
    print("Invalid search type. Please enter 1 for simple string search or 2 for domain search.")

