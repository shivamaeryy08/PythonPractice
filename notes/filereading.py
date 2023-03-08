# file = open('./filereading.txt')
# contents = file.read()
# print(contents)
# file.close()  # must close file after reading contents

with open('./filereading.txt', mode='w') as file:  # as meaning alias, no need to close manually using with
    # contents = file.read()
    # print(contents) #w = write mode, r = read mode, a = append
    file.write('meow')

# if file doesnt exist and u write, python creates the file



