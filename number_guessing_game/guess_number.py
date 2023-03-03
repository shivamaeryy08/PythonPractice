import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'hard' or 'easy: '")
computer_choice = random.randint(1,100)
if (difficulty == "hard"):
    number_attemps = 5
else:
    number_attemps = 10
continue_game = True    
guess = int(input("Make a guess: "))
while (continue_game):
    if (guess < computer_choice):
        print("Too low")
        print("Guess again")
        number_attemps-=1
        print(f"There are {number_attemps} attemps left")
    elif (guess > computer_choice):
        print("Too high")
        print("Guess again")
        number_attemps-=1
        print(f"There are {number_attemps} attemps left")
    else:
        print("You win")
        break
    if (number_attemps==0):
        continue_game=False
        print("You have run out of attempts, you lose!")
        print(f"The correct number was {computer_choice}")
    else:
        guess = int(input("Make a guess: "))


