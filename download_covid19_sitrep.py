import os
import time
import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports'


def get_report():
    """
    Download situation report from who.int for further analysis of data
    """

    res = requests.get(URL)
    soup = bs(res.text, 'html.parser')
    all_links = soup.find_all('a')
    report_links = (link.get('href') for link in all_links if 'Situation' in link.text)
    base_url = 'www.who.int'
    for link in report_links:
        time.sleep(5)
        os.system(f'wget -nc {base_url + link}')


if __name__ == '__main__':
    get_report()
