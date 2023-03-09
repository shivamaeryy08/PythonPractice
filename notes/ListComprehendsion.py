# new_list = [new_item for item in list]

numbers = [1, 2, 3, 4]

numbers_times_2 = [number * 2 for number in numbers]

print(numbers_times_2)

# can do this on a string to get every letter

# list range string tuple are sequences

final_list = [i * 2 for i in range(1, 5)]

# Conditional list comprehendsion


names = ['Shivam', 'Mike']

# new_list = [new_item for item in list if test]

names_4_characters = [name for name in names if len(name) == 4]

print(names_4_characters)
