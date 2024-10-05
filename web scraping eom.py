import requests
from bs4 import  BeautifulSoup

url="https://www.amazon.in/s?k=iphone&crid=36KI0QJ5EFEO9&sprefix=ipho%2Caps%2C372&ref=nb_sb_noss_2"
header= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r=requests.get(url,headers=header)
soup=BeautifulSoup(r.text,'html.parser')

#print(soup.prettify)

spans=soup.select("span.a-size-medium.a-color-base.a-text-nomral")



