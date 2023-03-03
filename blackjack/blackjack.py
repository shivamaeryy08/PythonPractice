from art import logo
import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print(logo)
def get_starting_cards(cards):
    player_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards = []
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    return [player_cards,computer_cards]

def compare(computer_score,player_score,player_cards,computer_cards):
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
    if (player_score >21):
        print("You lose, you went over 21, player bust")
    elif (computer_score == 21):
        print("Computer has reached blackjack, you lose")
    elif (computer_score > 21):
        print("You win, computer bust")
    elif (computer_score != 21 and player_score == 21):
        print("You reached blackjack, you win!")
    elif (player_score < 21 and computer_score < 21):
        if (player_score == computer_score):
            print("Draw")
        elif (player_score < computer_score):
            print("You lose")
        elif (player_score > computer_score):
            print("You win")

def player_draws(player_cards):
    next_card = random.choice(cards)
    player_cards.append(next_card)
    player_score = sum(player_cards)
    if (player_score > 21):
        if (next_card == 11):
            player_cards[-1] = 1
            player_score = sum(player_cards)       
    return [player_cards,player_score]

def computer_draws(computer_cards):
    computer_score = sum(computer_cards)
    while computer_score < 17:
        next_card = random.choice(cards)
        computer_cards.append(next_card)
        computer_score = sum(computer_cards)
        if (computer_score > 21):
            if (next_card == 11):
               computer_cards[-1] = 1
               computer_score = sum(computer_cards)
    return [computer_cards,computer_score]
        
def play_blackjack():
    play_game = True
    while play_game:
        player_cards = get_starting_cards(cards)[0]
        computer_cards = get_starting_cards(cards)[1]
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while (draw_card == "y"):
            player_info = player_draws(player_cards)
            player_cards = player_info[0]
            player_score = player_info[1]
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if (player_score > 21):
                draw_card = "n"
            else:
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")

        computer_info = computer_draws(computer_cards)
        computer_score = computer_info[1]
        computer_cards = computer_info[0]
        compare(computer_score,player_score,player_cards,computer_cards)
        if (input ("Do you want to play another game of blackjack (y/n): ") == "y"):
            play_game = False
            os.system("cls")
            play_blackjack()
        else:
            play_game = False
            print("Blackjack game has been terminated")

play_blackjack()
    



 

 


