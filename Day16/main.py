from turtle import Turtle, Screen
from prettytable import PrettyTable

felix = Turtle()
felix.shape("turtle")
felix.color("aquamarine4")
felix.forward(100)
my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# __init__(self) - Initializes attributes


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id="001", username="Felix")
user_2 = User(user_id="002", username="Onduru")
user_1.follow(user=user_2)
print(user_1.following)
print(user_2.followers)
