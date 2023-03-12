import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')


def generate_phonetics():
    name = input("Enter a name: ").strip()
    letters = [letter.upper() for letter in name]
    try:
        list_codes = [data[data['letter'] == letter]['code'].to_list()[0] for letter in letters]
    except IndexError:
        print("Enter a valid word with only letters when using this program")
        generate_phonetics()
    else:
        print(list_codes)
    finally:
        print("yessir")
