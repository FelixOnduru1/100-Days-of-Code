from turtle import Turtle, Screen
from prettytable import PrettyTable

# felix = Turtle()
# felix.shape("turtle")
# felix.color("aquamarine4")
# felix.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
