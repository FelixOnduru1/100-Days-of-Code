import pandas as pd

data = pd.read_csv("squirrel_data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)


cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(cinnamon_squirrels)

squirrel_count = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

squirrel_count_data = pd.DataFrame(squirrel_count)
squirrel_count_data.to_csv("squirrel_count.csv")
