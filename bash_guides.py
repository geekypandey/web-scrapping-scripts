import os

import requests
from bs4 import BeautifulSoup as bs

def main():
    """ This scripts downloads all the guides from the given URL in PDF format.The page contains the guides in many different formats"""

    URL = "http://tldp.org/guides.html"
    res = requests.get(URL)
    soup = bs(res.text,'html.parser')
    links = ["https://tldp.org/" + link.a['href'] for link in soup.find_all('li') if link.a.text.strip() == "PDF"]
    for link in links:
        os.system(f"wget -nc {link}") #using wget to download

if __name__ == "__main__":
    main()
