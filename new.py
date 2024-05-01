import requests
from bs4 import BeautifulSoup



URL = "https://sfbay.craigslist.org/search/los-gatos-ca/cta?lat=37.1836&lon=-121.95&max_price=10000&min_auto_year=2014&search_distance=18#search=1~gallery~0~0"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


# parsing gosterilmis link uzre

result = soup.find(class_="cl-static-search-results")
car_element = result.find_all('li', class_='cl-static-search-result')

for car_elem in car_element:
    title_elem = car_elem.find('div', class_='title') # title
    price_elem = car_elem.find('div', class_='price') #qiymet
    location_elem = car_elem.find('div', class_='location') # location
    url_elem = car_elem.find('a', href=True)['href'] #url gosterir


    print(title_elem.text.strip())
    print(price_elem.text.strip())
    print(location_elem.text.strip())
    print(url_elem)
    

  