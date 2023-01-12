import requests
from bs4 import BeautifulSoup

from tkinter import *
root.Tk()
root.geometry("400x500")
root.title("Corona Cases")
font("helvetica",14,"Bold")
url="https://www.worldometers.info/coronavirus/"
url1="https://www.worldometers.info/coronavirus/country/india/"
page=requests.get(url)
page1=requests.get(url1)
Soup=BeautifulSoup(page.content,"html.parser")
Soup1=BeautifulSoup(page1.content,"html.parser")

info = Soup.find_all(class_="maincounter-number")
info1 = Soup1.find_all(class_="maincounter-number")

print(info)
a=[items.get_text() for items in info]
b=[items.get_text() for items in info1]

print('Total cases of corono virus')
print(a[0])
print('Total deaths of coronavirus')
print(a[1])
print('Total recoverd people from coronavirus')
print(a[2])
print('Total cases of India')
print(b[0])
print('Total deaths in India')
print(b[1])
print('Total recoverd people in India')
print(b[2])
