import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10','11','12','13','14','15','16','17','18']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("Enter the number of letters: "))
number_numbers = int(input("Enter the number of numbers: "))
number_letters_symbols = int(input("Enter the number of symbols: "))
password = ""

for i in range(0, number_letters):
    password += random.choice(letters)
for i in range(0, number_numbers):
    password += random.choice(numbers)
for i in range(0, number_letters_symbols):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Your password is:", password)
