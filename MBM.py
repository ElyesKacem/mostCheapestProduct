from ProductClass import Nav
from bs4 import BeautifulSoup
import requests
from ProductClass import Product


def fillList(key):
    global request1,soup,products
    navObject=Nav("https://www.mbm-tn.com/jolisearch?poscats=0&s=msi&page=2",key)
    keepSearching=True
    i=1
    while(keepSearching):
        
        navObject.link=navObject.getLinkWithPage(i)
        print(navObject.link)
      
        request1 = requests.get(navObject.link)
        soup=BeautifulSoup(request1.text,'lxml')
        if(soup.find('h4',string="Veuillez nous excuser pour le désagrément.")):
            break
        else:
            products = soup.find_all('div',class_="item-product product_per_4 col-xs-12 col-sm-6 col-md-6 col-lg-4 col-xl-4")
            for product in products:
                title = product.find('a',class_="product_name one_line").text
                link=product.find('a',class_="product_name one_line")["href"]
                price = product.find('span',class_='price').text
                description=product.find('div',class_='product-desc').text.replace("\xa0","")
                #photo=product.find('img',class_="first-image ")["href"]
                #prod=Product(title,description,price,photo,link)
                photo=product.find('img',class_="first-image")["src"]
                prod=Product(title,description,price,photo,link)

                navObject.addToList(prod)
            i=i+1
    return navObject.listOfResult





