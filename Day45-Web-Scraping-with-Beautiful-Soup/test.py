from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as site:
    contents = site.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.a.get("href"))
# print(soup.find_all(name="a"))

heading = soup.find(name="h1", id="name")
print(heading)
