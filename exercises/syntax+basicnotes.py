print("SHivam " + "Aery") #concat using + 

#Input using input function

print("Shivam " + input("What is your name: "))

#to get length of string, use len(string)

#input and print add \n automatically at end

#Data types

#Access index of string

first_letter = "Shivam"[0]

 #can use -1 to access lasst number

print(first_letter)

#Integer

print(1234+438) #can add underscores like php for large integers

print(123_345)

#Float

3.14

#Boolean

True
False

#TypeChecking/TypeErrors

#PYTHOJN DOES NOT AUTOCONCANT INTS

#type() to get type of the input in betwen the type data

print("My favoirte number " + str(7))

#typeconversionn/type castikng

two_digit_number = input("Number")

print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Operations

#Division always gives a float, even if divides perfectly

print(6/3)

# ** = exponentiation

#ROUNDING, round takes number of precsion digits

print(round(8/3))

# // means floor division and gives floored integer

# F STRING auto concatenates non strings to string

name =89999

print(f"your name is {name}")

#IF ELSE SYNTAX

if name >400:
    print(name)

elif name <500:
    print("ow") 

else:
    pass

print("sadve")

#LOGICAL OPERATORS

# and or, to do multiline string, use ''' at beginnnign and end