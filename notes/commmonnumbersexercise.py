with open('file1.txt') as file:
    list_1 = [number.rstrip('\n') for number in file.readlines()]

with open('file2.txt') as file:
    list_2 = [number.rstrip('\n') for number in file.readlines()]

list_common_integers = [int(number) for number in list_1 if number in list_2]
print(list_common_integers)
