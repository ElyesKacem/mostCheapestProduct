class Product:
  def __init__(self, title, description,price,photo,link):
    self.photo=photo
    self.title = title
    self.link=link
    self.description = description
    self.price=price
   
    

class Nav:
  def __init__(self,link,title):
    self.title=title
    # decomposedLink=link.split("&")
    # print(decomposedLink)
    # a=self.lookLike('s=',decomposedLink)
    # print(a)
    # if(a==-1):
    #   raise ValueError("didn't find the search attribut from the link")
    # decomposedLink[a]="s="+title
    # # print(decomposedLink)
    # link="&".join(decomposedLink)
    # # print(link)
    # print(title)
    link=link+"&"+title
    self.link=link
    # print(link)
    self.listOfResult=[]

  def lookLike(self,ch,list):
        for i in range(len(list)):
            if(ch in list[i]):
                return i
        return -1


  def getLinkWithPage(self,i):
    
    # decomposedLink=self.link.split("&")
    # b=self.lookLike('page=',decomposedLink)
    # if(b==-1):
    #     raise ValueError("didn't find the page attribut from the link")
    # decomposedLink[b]="page="+str(i)
    # return "&".join(decomposedLink)
    self.link=self.link+"&page="+str(i)
    return self.link


  def addToList(self,product):
    self.listOfResult.append(product)
    
  # def ifTheElementExist(self,notExistTag)

  # def fillTheList(self,i,productTag,productClass,notExistTag,notExistingString):
  #   keepSearching=True
  #   i=0
  #   while(keepSearching):
  #     self.link=self.getLinkWithPage(i)
  #     request1 = requests.get(self.link)
  #     soup=BeautifulSoup(request1,'lxml')
  #     if(soup.find(notExistTag,string=notExistingString)):
  #       break
  #     else:
  #       products = soup.find_all(productTag,class_=productClass)
  #       for product in products:
  #         pass

        


    