import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")
other_bidders = "yes"
bidders = {}
bids = []
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid: $"))
    bidders[name] = {"bid": bid}
    bids.append(bid)
    other_bidders = input("Are there any other bidders? Type yes or no: ").lower()
    os.system("cls")

max_bid = max(bids)

winner = []
for keys in bidders:
    if bidders[keys]["bid"] == max_bid:
        winner.append(keys)

if len(winner) > 1:
    print("There was a tie!")
else:
    print("The winner of the auction is", winner[0])
