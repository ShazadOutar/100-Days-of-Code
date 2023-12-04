import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_list_page = response.text

soup = BeautifulSoup(movies_list_page, "html.parser")
# print(soup.prettify())
# movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# print(movies)
# print(len(movies))
# print(movies[0].getText().split(") "))
# movies = [movie.getText().split(") ") for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
print(movies)
print(len(movies))

# write the movies list to the movie file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    # file.write("line 1\n")
    for movie in movies[::-1]:
        # file.write(f"{movie[0]}) {movie[1]}\n")
        file.write(movie + '\n')
