import random


def deal_card():
    """Returns random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the scores of the user and the computer to determine winner."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose. Opponent has a Blackjack."
    elif user_score == 0:
        return "You win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "The computer went over. You win!"
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    """Plays the game."""
    user_cards = []
    computer_cards = []
    game_active = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_active:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} and your current score is: {user_score}.")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_active = False
        else:
            another_card = input("Do you want another card?\nType 'y' for yes or 'n' for no:\n")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_active = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}. And your final score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards}. It's final score is: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the BlackJack Game?\nType 'y' for yes and 'n' for no:\n") == "y":
    play_game()
