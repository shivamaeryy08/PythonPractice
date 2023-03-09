sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

words = sentence.split(' ')

words_dict = {f'{word}': len(word) for word in words}

print(words_dict)
