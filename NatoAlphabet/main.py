import pandas

name = input("Enter a name: ").strip()
letters = [letter.upper() for letter in name]

data = pandas.read_csv('nato_phonetic_alphabet.csv')

list_codes = [data[data['letter'] == letter]['code'].to_list()[0] for letter in letters]

print(list_codes)
