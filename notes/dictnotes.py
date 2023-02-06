dict = {
    "name": "Shivam",
    "height": 100,
}

# access value

name = dict["name"]
height = dict["height"]

# add value

dict["favgame"] = "Persona"
print(dict)

# make empty dict

empty_dictionary = {}

# Wipe am existing dictionary

# dict = {}

# Edit item in dict

dict["name"] = "Joker"

# Loop through dictionary, loops through keys

for keys in dict:
    print(keys)

# Nesting

capitals = {
    "FRANCE": "PARIS",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {"France": ["Paris", "Lillie", "Dijon"]}

# Nesting dict in dict

travel_log_city = {
    "France": {"Visited": ["Paris", "Lillie", "Dijon"], "total_#_visits": 12}
}

print(travel_log_city["France"]["total_#_visits"])

# Can Nesting dict in list

dict1 = {}
dict2 = {}
