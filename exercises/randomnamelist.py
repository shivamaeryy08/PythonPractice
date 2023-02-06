#Program that takes list of names and returns stirng with one name randomly chosen

import random

list_of_names = input("Enter the list of names: ").split(", ")

choice = random.choice(list_of_names)

print(choice + " will order the meal tonight")


