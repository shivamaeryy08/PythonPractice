import random
import hangmanart
from hangmanwords import word_list


stages = hangmanart.stages


def getMatchingCharacterIndices(word, letter):
    indices_found = []
    for i in range(len(word)):
        if word[i] == letter:
            indices_found.append(i)

    return indices_found


end_of_game = False
winner = False
lives = 6
word = random.choice(word_list)
print(word)
underscore_list = len(word) * ["_"]
print(hangmanart.logo)
print(stages[6])
stage = 6
guess = input("Enter a letter:").lower()
while not end_of_game:
    if word.count(guess) > 0:
        if guess in underscore_list:
            print("You have already succesfully guessed:", guess)
        indices_of_letter = getMatchingCharacterIndices(word, guess)
        for indice in indices_of_letter:
            underscore_list[indice] = guess
        print(" ".join(underscore_list))
        if "".join(underscore_list) == word:
            end_of_game = True
            winner = True
        else:
            guess = input("Guess a letter:")

    else:
        lives -= 1
        stage -= 1
        print(stages[stage])
        print(f"The letter {guess} is not in the chosen word")
        print("Lives left:", lives)
        if lives == 0:
            break
        guess = input("Enter a letter:")

if winner:
    print("You won!")
else:
    print("You lost")
