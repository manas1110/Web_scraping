import requests
def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)

url="https://timesofindia.indiatimes.com/city/delhi/delhi-development-authority-dda-launches-new-housing-schemes-with-green-developments/articleshow/113764092.cms"
fetchAndSaveToFile(url,"data/times.html")