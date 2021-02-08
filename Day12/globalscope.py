# Modifying global scope
enemies = 1


def increase_enemies():
    return enemies + 1


enemies = increase_enemies()
print(enemies)

# Global constants
PI = 3.14159
URL = "https://www.google.com"


def area_circle(radius):
    global PI
    return PI * radius ** 2


print(area_circle(7))
