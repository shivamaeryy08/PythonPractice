import random

# make dict using list comprehsnion

# new_dict = {new_key: new_value for item in list}

# dict comprehension

# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

names = ['Shivam', 'Mike']

student_dict = {f'{name}\'s score': random.randint(0, 100) for name in names}

print(student_dict)

student_dict_double = {f'{key}\'s double score: ': value * 2 for (key, value) in student_dict.items()}

print(student_dict_double)
