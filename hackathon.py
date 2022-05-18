import requests
# from bs4 import BeautifulSoup as bs
# import csv

# HOST = "https://www.mashina.kg"
from datetime import datetime

def get_time(func):
    start = datetime.now()
    func()
    end = datetime.now()
    return f"request execution time {start - end}"

URL = "https://www.google.com/?hl=ru"

def get_html(URL):
    r = requests.get(URL)
    return r.text

get_html = get_time(get_html)
get_html()

# print(get_html(URL))

# get_html(URL)
# html = get_html(URL)


# def get_content(html):
#     soup = bs(html, 'lxml')
#     cars = soup.find_all("div", class_ = "list-item list-label")
    # print(cars)
    # links = []
    # discs = soup.find_all('a', href = '/details/')
    # for disc in discs:
    #     links.append(disc.find('h2', class_ ='comment'))

    # print(links)
#     for car in cars:
#         try:
#             brand = car.find('h2', class_ = 'name').text.split()
#         except:
#             brand = "brand not found"
#         try:
#             image = HOST + car.find('img', class_ = 'lazy-image').get('data-src')
#         except:
#             image = "image not found"
#         try:
#             price = car.find('p', class_ = 'price')
#             print(price)
#         except:
#             price = "price not found"
#         try:
#             discs = soup.find('div', class_ = 'block info-wrapper item-info-wrapper').text.replace('\n', '').strip()
#         except:
#             discs = 'discription not found'

#         data = {
#                 'brand': brand, 
#                 'image': image,
#                 'price': price,
#                 'description':discs,
#                 }
#         save_info(data)

        
# def save_info(data):
#     with open('moto.csv', 'a') as file:
#         writer = csv.writer(file, delimiter =",")
#         writer.writerow((data['brand'], data['image'], data['price'], data['description']))

# def main():
#     for page in range(1, 3):
#         print(f"parsing {page} page")
#         url = f"https://www.mashina.kg/search/bmw/all/?currency=2&sort_by=upped_at+desc&time_created=all&page={page}"
#         html = get_html(url)
#         get_content(html)

# main()