from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

request0 = urlopen('https://www.tunisianet.com.tn/')
soup = BeautifulSoup(request0,'lxml')
"""if ' ' in keyword:
    keyword = keyword.replace(' ','+')
    request0 = requests.get('https://www.tunisianet.com.tn/recherche?controller=search&orderby=price&orderway=asc&s='+keyword+'&submit_search=').text
else:
    request0 = requests.get('https://www.tunisianet.com.tn/recherche?controller=search&orderby=price&orderway=asc&s='+keyword+'&submit_search=').text
print(keyword)
soup = BeautifulSoup(request0,'lxml')
print(soup.prettify)
products = soup.find_all('tr',class_= 'item product product-item product-item-info')
for product in products:
    name = product.find('h2',class_="h3 product-title").find('a').text
    price = product.find('span',class_='price').text
    #ref = product.find('span',itemprop='sku').text
    print("PRODUIT:",name.text,"PRIX:",price)
    print("Link: ",name.get('href'))
    #print("reference: ",ref)"""