import requests
from bs4 import BeautifulSoup
import os

os.system('clear')

product_name = input("Enter the product name: ")
product_name = product_name.replace(" ", "+")
discount = int(input("Enter dicount number(0 or greater): "))
wanted_price = int(input("Highest price for the item0 or greater: ").strip())

# make a GET request to the URL
response = requests.get(f'https://www.jumia.ug/catalog/?q={product_name}')

# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# find all the products on the page
products = soup.find_all('div', {'class': 'info'})

#print(products)

for product in products:
    # find the discount percentage of the product
    discount_tag = product.find('div', {'class': 'bdg _dsct _sm'})
    #print(discount_tag)
    if discount_tag is None:
        continue
    discount_percent = int(discount_tag.text.replace('%', '').strip())

    # check if the discount percentage is above 50%
    if discount_percent > discount or discount == 0:
        #print(discount_percent)
        # get the name and price of the product
        name_tag = product.find('h3', {'class': 'name'})
        name = name_tag.text.strip()
        
        price_tag = product.find('div', {'class': 'prc'})
        price = price_tag.text
        prices = price.strip()
        ugx_removed = price.replace('UGX', '').replace(',', '')

        #print(int(ugx_removed)) 

        if int(ugx_removed) < wanted_price or wanted_price == 0:
            # print the information about the product
            print(f'{name} ({discount_percent}% off): {prices}')
        
