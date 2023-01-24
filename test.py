import requests
from bs4 import BeautifulSoup

# specify the domain you want to search for
domain = "mcblend.fr"

# send the request to Google
response = requests.get(f"https://www.google.com/search?q=site:{domain}")

# parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# extract the search results
results = soup.find_all("div", class_="r")

# print the results
for result in results:
    print(result.a["href"])

