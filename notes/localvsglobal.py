#No block scope

if 3 > 2:
    a_variable = 10 # has global scope not block level like in java, only fucntionns define local scope, inclduing for while dont matter


#Modify global variable  
 

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2

    print(enemies)

increase_enemies()

#Global constants

PI = 3.14159


