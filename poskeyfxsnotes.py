#positional argument means ordering MATTERS in arguments, argument goes to corresponding position in fx call

def greet_with_pos(name,location):
    print(f"Hi {name} located at {location}")

greet_with_pos("Shivam","Canada")

#keyword argumwent means you can specify which argument correpsonds to which parameter

def greet_with_key(name,location):
    print(f"Hi {name} located at {location}")

greet_with_key(name="Shivam",location="Canada") 