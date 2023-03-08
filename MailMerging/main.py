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
