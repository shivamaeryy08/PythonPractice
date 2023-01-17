#list syntax

states_of_america = ["Delaware", "Pennslyvania", "Oklahoma", "Alaska"] #inside of list can be diff types

#how to order a list

#print first element

print(states_of_america[0])

#can use negative index 

print(states_of_america[-1])

#change element

states_of_america[0] = "Washington"

print(states_of_america[0])

#can just print list directly

#add to end of list

states_of_america.append("Indiana")

print(states_of_america)

#.extend allows u to extend list by inputted list

#nested list

fruits = ["Apple", "Banana", "Orange"]
vegtables = ["Tomato", "Potato", "Carrot"]

food = [fruits,vegtables]

print(food)






