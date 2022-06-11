from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar,Scrollbar
from turtle import width
from unittest.mock import DEFAULT
from PIL import ImageTk, Image
from threading import Thread
import tkinter.font as font
import MBM
import SBS

root = Tk()
root.title("better than google")
root.minsize(800,500)
root.iconbitmap("search_find_window_16723.ico")


searchFrame = Frame(root)

f = font.Font(weight="bold",size=12)
ff = font.Font(weight="bold",size=10)
entry = Entry(searchFrame,width=30,font=ff)
entry.insert(0,"what you looking for")
search = Label(searchFrame,text="Search: ",font=f)
searchButton = Button(searchFrame,text="Search",padx=10,pady=2,command = lambda: Search(entry.get()),font=ff)
result = Label(searchFrame)
image = ImageTk.PhotoImage(Image.open("logo3.png"))
logo = Label(searchFrame,image=image)

logo.grid(row=0,column=0,columnspan=3,pady=20)
search.grid(row=1,column=0,sticky=E,pady=20)
entry.grid(row=1,column=1,columnspan=2,sticky=W,pady=20)
searchButton.grid(row=2,column=1,pady=5)
result.grid(row=3,column=1)


"""loadingFrame = Frame(root,height=root.winfo_height(),width=root.winfo_width())

progressBar = Progressbar(loadingFrame, orient=HORIZONTAL, length=300, mode="determinate")
progressBar.place(relx=.5, rely=.5,anchor= CENTER)
progressBar.pack()

intermediatB = Button(loadingFrame,text="progress",padx=10,pady=1,command=progress)
intermediatB.pack()"""

mainFrame = Frame(root,height=root.winfo_height(),width=root.winfo_width())

scrollCanva = Canvas(mainFrame,height=root.winfo_height(),width=root.winfo_width())
scrollCanva.pack(side=LEFT,fill=BOTH,expand=1)

scrollBar = ttk.Scrollbar(mainFrame,orient=VERTICAL,command=scrollCanva.yview)
scrollBar.pack(side=RIGHT,fill=Y)

scrollCanva.configure(yscrollcommand=scrollBar.set,scrollregion=scrollCanva.bbox("all"))
scrollCanva.bind('<Configure>',lambda e: scrollCanva.configure(scrollregion=scrollCanva.bbox('all')))

listFrame = Frame(scrollCanva,height=root.winfo_height(),width=root.winfo_width())

scrollCanva.create_window((0,0),window=listFrame,anchor=NW)
#listFrame.pack()
#data=[{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'hi','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'hi','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'hi','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'hi','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545},{'nom':'msi gl65 leopard','link':'sdddddddddddgdfgdfsgffdg','prix':4545}]
image2 = ImageTk.PhotoImage(Image.open("logo3.png"))
data=[]
def Search(keyword):
    data=MBM.fillList(keyword)+SBS.fillList(keyword)
    def getKey(obj):

        obj.price=obj.price.replace('TND',"").replace(",",".").replace(" ","").replace("\xa0","")


        return float(obj.price)
    data.sort(key=getKey)
    searchFrame.pack_forget()
    f = font.Font(weight="bold",size=12)
    for item in data:
        itemFrame = Frame(listFrame,height=root.winfo_height(),width=root.winfo_width(),pady=5)
        logo2 = Label(itemFrame,image=image2)
        logo2.grid(row=0,column=0,rowspan=5)
        nom= Label(itemFrame,text=item.title)
        nom['font']=f
        prix= Label(itemFrame,text=item.price,font=("Arial",15 ),fg="green")
        description = Text(itemFrame,wrap='word',width=82,height=4 ,bg=root.cget('bg'))
        description.insert(1.0,item.description)
        description.config(state=DISABLED)
        link= Label(itemFrame,text="Plus de details: "+item.link,wraplength=500,justify="left")
        nom.grid(row=0,column=1,sticky=W)
        prix.grid(row=0,column=3,sticky=E)
        description.grid(row=1,column=1,columnspan=4)
        link.grid(row=2,column=1,sticky=W)
        itemFrame.pack()
    mainFrame.pack()
    #Thread(target=zoom.zoom(keyword)).start()
    #print("sheiss")



searchFrame.pack()

root.mainloop()