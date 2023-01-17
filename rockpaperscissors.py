# Simple rock paper scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")

print("You chose: ")

if player_input == "0":
    player_input = "rock"
    print(rock)
elif player_input == "1":
    player_input = "paper"
    print(paper)
else:
    player_input = "scissors"
    print(scissors)

random_int = random.randint(0, 2)
computer_choice = 0
if random_int == 0:
    computer_choice = "rock"
elif random_int == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

print("Computer chose:")

if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)


if player_input == computer_choice:
    print("It's a tie!")

elif player_input == "rock" and computer_choice == "scissors":
    print("You win!")

elif player_input == "paper" and computer_choice == "rock":
    print("You win!")

elif player_input == "scissors" and computer_choice == "paper":
    print("You win!")

elif player_input == "scissors" and computer_choice == "rock":
    print("You lose!")

elif player_input == "paper" and computer_choice == "scissors":
    print("You lose!")

elif player_input == "rock" and computer_choice == "paper":
    print("You lose!")
