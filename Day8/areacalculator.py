import math
print("Welcome to the Paint Calculator.\n"
      "This program helps you calculate the area you're going to paint "
      "and tells you the amount of cans of paint that you will need.")


def paint_calculator(width, height):
    area = width * height
    cans_of_paint = math.ceil(area/5)
    print(f"The area to be painted is {area} square metres.\n"
          f"You will need to buy {cans_of_paint} cans of paint.")


width_entry = int(input("What is the width of your wall in metres?\n"))
height_entry = int(input("What is the height of your wall in metres?\n"))
paint_calculator(width=width_entry, height=height_entry)
