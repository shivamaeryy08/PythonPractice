# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as file_names:
    list_names = []
    for name in file_names.readlines():
        name = name.rstrip('\n')
        list_names.append(name)

with open('./Input/Letters/starting_letter.txt') as template:
    template = template.read()

for name in list_names:
    with open(f'./Output/ReadyToSend/LetterTo{name}.txt', 'w') as letter:
        customized_letter = template.replace('[name]', name)
        letter.write(customized_letter)
