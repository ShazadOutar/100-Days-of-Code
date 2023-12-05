from bs4 import BeautifulSoup
import requests

# input_date = input("Which date to use? Please enter a date in the format YYYY-MM-DD")
input_date = "2022-11-19"

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{input_date}")
billboard_site = response.text

soup = BeautifulSoup(billboard_site, "html.parser")
# print(soup.prettify())
# songs = soup.find_all(name="h3", id="title-of-a-story")
# print(songs)
# print(len(songs))
# print(songs[0].getText())
# print(soup.find(name="h3", id="title-of-a-story"))
# print(songs[3])

# print(soup.select_one(selector="body"))
print(soup.find(name="div", class_="o-chart-results-list-row-container").find_all(name="li")[3].find(name="h3").getText().strip())
song_tags = soup.find_all(name="div", class_="o-chart-results-list-row-container")
print(len(song_tags))
song_names = [song.find_all(name="li")[3].find(name="h3").getText().strip() for song in song_tags]
print(song_names)

