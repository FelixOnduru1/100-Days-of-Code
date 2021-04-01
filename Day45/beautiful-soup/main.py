from bs4 import BeautifulSoup
# import lxml
with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Alternatively, depending on the website you can use lxml as:
# soup = BeautifulSoup(contents, "lxml")

all_lists = soup.find_all(name="li")
for list_item in all_lists:
    print(list_item.getText())
