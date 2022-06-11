from bs4 import BeautifulSoup
import requests

#browser = webdriver.Chrome()
#browser.get('https://www.mytek.tn/informatique/ordinateurs-portables/pc-gamer.html?product_list_limit=all')

keyword = input('search: ')

if ' ' in keyword:
    keyword = keyword.replace(' ','+')
    request0 = requests.get('https://www.mytek.tn/catalogsearch/result/?q='+keyword+'&product_list_limit=all').text
    print(request0)
else:
    request0 = requests.get('https://www.mytek.tn/'+keyword+'?product_list_limit=all').text
    print(request0)
print(keyword)
soup = BeautifulSoup(request0,'lxml')
print(soup.prettify)
products = soup.find_all('tr',class_= 'item product product-item product-item-info')
"""for product in products:
    name = product.find('a',class_='product-item-link')
    price = product.find('span',class_='price').text
    ref = product.find('span',itemprop='sku').text
    print("PRODUIT:",name.text,"PRIX:",price)
    print("Link: ",name.get('href'))
    print("reference: ",ref)"""