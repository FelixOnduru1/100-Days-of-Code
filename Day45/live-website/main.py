from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
yc_story_titles = soup.find_all(name="a", class_="storylink")

titles = []
links = []
for title in yc_story_titles:
    article_title = title.getText()
    article_link = title.get("href")
    titles.append(article_title)
    links.append(article_link)

yc_story_scores = soup.find_all(name="span", class_="score")

scores = [int(score.getText().split(" ")[0]) for score in yc_story_scores]

highest_score_index = scores.index(max(scores))
print(titles[highest_score_index])
print(links[highest_score_index])

