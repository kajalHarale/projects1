from tkinter import *
import requests
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/"
page=requests.get(url)
Soup=BeautifulSoup(page.content,"html.parser")
info = Soup.find_all(class_="maincounter-number")
a=[items.get_text() for items in info]

country=""


root=Tk()

root.title("Corona Reports")
root.geometry("500x500")
font=("helvetica",14,"bold")


def  find_info():
    country=c.get()
    url1="https://www.worldometers.info/coronavirus/country/" +country
    page1=requests.get(url1)
    Soup1=BeautifulSoup(page1.content,"html.parser")
    info1 = Soup1.find_all(class_="maincounter-number")
    b=[items.get_text() for items in info1]

    label1=Label(root,font=font,text='Total cases of corono virus'  +country)
    label1.pack()

    label1=Label(root,font=font,text=b[0])
    label1.pack()

    label1=Label(root,font=font,text='Total deaths of coronavirus'  +country)
    label1.pack()

    label1=Label(root,font=font,text=b[1])
    label1.pack()

    label1=Label(root,font=font,text='Total recoverd people from coronavirus'  +country)
    label1.pack()

    label1=Label(root,font=font,text=b[2])
    label1.pack()



label1=Label(root,font=font,text='Total cases of corono virus')
label1.pack()

label1=Label(root,font=font,text=a[0])
label1.pack()

label1=Label(root,font=font,text='Total deaths of coronavirus')
label1.pack()

label1=Label(root,font=font,text=a[1])
label1.pack()

label1=Label(root,font=font,text='Total recoverd people from coronavirus')
label1.pack()

label1=Label(root,font=font,text=a[2])
label1.pack()

label1=Label(root,font=font,text="Please Enter Country Name:-")
label1.pack()
c=Entry(root,font=font)
c.pack()

button1=Button(root,font=font,text="Find Info",bg="green",command=find_info)
button1.pack()


root.mainloop()
