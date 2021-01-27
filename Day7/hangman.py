import random
from hangman_art import logo
from word_list import word_list
print(logo)
print("Welcome to the Hangman Game!")

random_word = random.choice(word_list)
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

game_status = True
blank_spaces = []
progress = ""
lives = 6

for letter in random_word:
    blank_spaces += "_"
print(stages[0])
while "_" in blank_spaces and lives > 0:
    guess = input("Guess a letter:\n").lower()
    blanks_counter = 0
    blanks_before = blanks_counter + blank_spaces.count("_")
    for position in range(len(random_word)):
        letter = random_word[position]
        if guess == letter:
            blank_spaces[position] = guess
    blanks_after = blank_spaces.count("_")
    if blanks_before > blanks_after:
        lives += 0
        print(stages[6-lives])
    else:
        lives -= 1
        print(stages[6-lives])
    if "_" not in blank_spaces and lives != 0:
        print("You win!!")
    elif "_" in blank_spaces and lives == 0:
        print("You lose!")
        print(f"The word was {random_word}.")
    print(f"{' '.join(blank_spaces)}")
