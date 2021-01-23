import random
print("Welcome to Rock, Paper, Scissors. Play against the computer and try to win.")
selection = input("Make a selection. Rock, Paper or Scissors?\n").lower()
rock_image = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper_image = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors_image = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
selection_value = 0
if selection == "rock":
    selection_value += 0
    print(rock_image)
elif selection == "paper":
    selection_value += 1
    print(paper_image)
elif selection == "scissors":
    selection_value += 2
    print(scissors_image)
else:
    print("Please type a valid entry. Rock was selected for you.")
computer_selection = random.randint(0, 2)
print("Computer chose:\n")
if computer_selection == 0:
    print(rock_image)
elif computer_selection == 1:
    print(paper_image)
else:
    print(scissors_image)
if computer_selection == selection_value:
    print("This round was a draw.")
elif selection_value == 0 and computer_selection == 2:
    print("You win this round!")
elif selection_value == 1 and computer_selection == 0:
    print("You win this round!")
elif selection_value == 2 and computer_selection == 1:
    print("You win this round!")
else:
    print("Computer wins this round. You lose!!")
