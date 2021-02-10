from art import logo
import random


def assign_lives(game_level):
    if game_level == "easy":
        num_lives = 10
        return num_lives
    elif game_level == "hard":
        num_lives = 5
        return num_lives
    else:
        print("You typed an invalid entry.")


def life_counter(num_lives):
    num_lives += -1
    if num_lives == 0:
        print(f"You have run out of lives. The number was {actual_number}")
    elif num_lives == 1:
        print(f"You have only {num_lives} attempt left")
    else:
        print(f"You have {num_lives} attempts left.")
    return num_lives


print(logo)
print("Welcome to the Number Guessing Game!!")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficult: Easy or hard?\n").lower()

lives = assign_lives(game_level=level)
game_active = True
actual_number = random.randint(1, 100)

while game_active:
    if lives >= 1:
        game_active = True
        user_guess = int(input("Make a guess:\n"))
        the_difference = user_guess - actual_number
        if the_difference == 0 and lives > 0:
            print(f"You guessed it right. The number was {actual_number}")
            game_active = False
        elif the_difference != 0 and lives == 1:
            game_active = False
            lives = life_counter(num_lives=lives)
        elif the_difference > 0 and lives > 0:
            print("The number you guessed is too high.")
            game_active = True
            lives = life_counter(num_lives=lives)
        elif the_difference < 0 < lives:
            print("The number you guessed is too low.")
            game_active = True
            lives = life_counter(num_lives=lives)
    else:
        game_active = False
