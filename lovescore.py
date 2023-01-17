# Program that tests compatibility bet two ppl based on occurences of letters t,r,u,e and l,o,v,e

first_name = input("Enter the First Person's Name: ")
second_name = input("Enter the Second Person's Name: ")

combined_name = first_name.lower() + " " + second_name.lower()

number_of_t = combined_name.count('t')
number_of_r = combined_name.count('r')
number_of_u = combined_name.count('u')
number_of_e = combined_name.count('e')
totaltrue_as_string = str(
    number_of_t + number_of_r + number_of_u + number_of_e)

number_of_l = combined_name.count('l')
number_of_o = combined_name.count('o')
number_of_v = combined_name.count('v')
number_of_e = combined_name.count('e')
totallove_as_string = str(
    number_of_l + number_of_o + number_of_v + number_of_e)

score = totaltrue_as_string + totallove_as_string

score_as_int = int(score)

if (score_as_int < 10 or score_as_int > 90):
    print(
        f"Your score is {score_as_int}, you go together like coke and mentos")
elif (score_as_int > 40 and score_as_int < 50):
    print(f"Your score is {score_as_int}, you are alright together")
else:
    print(f"Your score is {score_as_int}")
