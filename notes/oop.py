# What we did so far is procedural programming top-down programming paradigm

# OOP is a paradigm

# Class has attributes and methods, each instance of the class is a object, class is blueprint

# each letter capitalized is pascal case for a object instancwe, no new keyword needed

from turtle import Turtle, Screen

from prettytable import PrettyTable


# table = PrettyTable()
# xyla = Turtle()
# xyla.shape("turtle")
# xyla.color('red', 'blue')
# xyla.forward(100)
# screen = Screen()
# print(screen.canvwidth)
# screen.exitonclick()


class User:
    def __init__(self, id, username):
        self.id = id  # setting attriubte of class
        self.username = username
        self.followers = 0
        self.following = 0  # default attributes

    def follow(self, user):  # have to have self as first parameter to know object taht called it
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "shiv"

# print(user_1.id)

# Initizaling object means creating objecvt with certai values
user_1 = User(3, "xyla")
user_2 = User(5, "shivam")  # self is the object
user_2.follow(user_1)
print(user_2.following)
print(user_1.followers)
