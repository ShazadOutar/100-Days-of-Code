from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.find(class_="athing").find(class_="title").get("a"))
# article_text = soup.find(class_="athing").find_all(class_="title")[-1].getText()

# Find the info for the first
article_tag = soup.find(name="span", class_="titleline").find("a")
# print(soup.find(name="a"))
article_text = article_tag.getText()
article_link = article_tag.get("href")
# print(article_tag)
# print(article_text)
# print(article_link)
article_score = soup.find(name="span", class_="score").getText()
# print(article_score)

# Get all article titles, links, and up-votes
articles = soup.find_all(name="span", class_="titleline")
article_titles = []
article_links = []
for article in articles:
    # get the article tags with the article info
    article_tag = article.find("a")
    title = article_tag.getText()
    article_titles.append(title)
    link = article_tag.get("href")
    article_links.append(link)

print(article_links)
print(article_titles)

# article_upvotes = []
# for score in soup.find_all(name="span", class_="score"):
#     print(score.getText())

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)

highest_upvotes_index = article_upvotes.index(max(article_upvotes))
highest_article = (article_titles[highest_upvotes_index],
                   article_links[highest_upvotes_index],
                   article_upvotes[highest_upvotes_index])

print(highest_article)
