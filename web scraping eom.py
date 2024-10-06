import requests
from bs4 import  BeautifulSoup

url="https://www.imdb.com/search/title/?title_type=feature&primary_language=en&sort=num_votes,desc"
header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

r=requests.get(url,headers=header)
soup=BeautifulSoup(r.text,'html.parser')
#print(soup.prettify())
#print(soup.prettify)
#links = soup.select('a.ipc-poster-card__title.ipc-poster-card__title--clamp-2.ipc-poster-card__title--clickable.sc-e87ae275-1.kwafyq.gli-title')
links=soup.find_all('h3', class_="ipc-title__text")
# Get the text content of all found tags
movie_title=[]
for link in links:
    movie_title.append(link.get_text())

links=soup.find_all('span' ,class_="sc-ab348ad5-8 cSWcJI dli-title-metadata-item")
# Get the text content of all found tags
i=0
year=[]
time=[]
rating=[]
for link in links:
    if i%3==0:
        year.append(link.get_text())
    if i%3==1:
        time.append(link.get_text())
    if i%3==2:
        rating.append(link.get_text())
    i+=1
links=soup.find_all('span', class_="ipc-rating-star--rating")
# Get the text content of all found tags
movie_rating=[]
for link in links:
    movie_rating.append(link.get_text())
for i in range(len(year)):
    print(movie_title[i]," ",year[i]," ",time[i]," ",rating[i])
    print(f"its rating by users is {movie_rating[i]}")
    print()





