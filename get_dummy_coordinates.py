import requests
from bs4 import BeautifulSoup as bs

def get_points():
    for x in range(1,9):
        url = f'https://www.latlong.net/category/cities-102-15-{x}.html'
        res = requests.get(url)
        soup = bs(res.text,'html.parser')
        row = soup.find_all('tr')
        for x in row:
            td = x.find_all('td')
            coord = [y.text for y in td]
            print(coord)

if __name__ == '__main__':
    get_points()
