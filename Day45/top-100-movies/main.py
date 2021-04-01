from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all(name="img", class_="jsx-952983560 loading")

movie_titles = [movie.get("alt") for movie in movies if movie.get("alt") != ""]
movie_titles.remove("The Godfather")

# Or movie_titles[::-1] for reversing
movie_titles.reverse()
print(movie_titles)
item = 0
with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        item += 1
        file.write(f"{item}) {movie}\n")
