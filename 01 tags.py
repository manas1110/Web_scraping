import requests
from bs4 import BeautifulSoup
with open("sample.html","r") as f:
    html_doc=f.read()
soup=BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div")[0])

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# s=soup.find(id="link4")
# print(s.get("href"))

# print(soup.select("div.italic"))

# for child in soup.find(class_="container").children:
#     print(child)
# for parent in soup.find(class_="child").parents:
#     print(parent)
#     break

# cont=soup.find(class_="container")
# cont.name="span"
# cont.string="I am a string"

# ultag=soup.new_tag("ul")
# litag=soup.new_tag("li")
# litag.string="home"
# ultag.append(litag)

# soup.html.body.insert(0,ultag)
# with open("modified.html" ,"w") as f:
#     f.write(str(soup))

cont=soup.find(class_="container")
print(cont.has_attr("class"))

