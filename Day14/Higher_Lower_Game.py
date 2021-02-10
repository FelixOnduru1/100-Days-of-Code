import random
from game_art import logo
from game_art import versus
from game_data import data


def printable_description(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"


print("Welcome to the Higher Lower Game.\n"
      "In this game you will try to guess who has the highest number of Instagram followers.\n"
      "The games ends as soon as you get it wrong.")
print(logo)

user_A_details = random.choice(data)
game_active = True
score = 0

while game_active:

    user_B_details = random.choice(data)

    if user_A_details == user_B_details:
        user_B_details = random.choice(data)

    else:
        print(f"Compare A: {printable_description(account=user_A_details)}")
        print(versus)
        print(f"Against B: {printable_description(account=user_B_details)}")
        player_answer = input("Who has more followers? Type 'A' or 'B':\n").lower()
        if player_answer == "a":
            if user_A_details["follower_count"] > user_B_details["follower_count"]:
                score += 1
                print(f"You're right. Your current score is {score}")
            else:
                print(f"Sorry, that's wrong. Your final score is {score}")
                game_active = False
        elif player_answer == "b":
            if user_B_details["follower_count"] > user_A_details["follower_count"]:
                score += 1
                print(f"You're right. Your current score is {score}")
            else:
                print(f"Sorry, that's wrong. Your final score is {score}.")
                game_active = False
    user_A_details = user_B_details
