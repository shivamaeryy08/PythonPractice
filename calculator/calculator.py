from art import logo

print(logo)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def subtract(x, y):
    return x - y


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    first_num = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)
    continue_calc = True    
    while continue_calc:
        symbol = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        answer = operators[symbol](first_num, next_num)
        print(f"{first_num} {symbol} {next_num} = {answer}")
        if input(f"Do you want to continue using the calculator using {answer} ? Enter yes or no: ") == "yes":
             first_num = answer
        elif (input ("Do you want to continue using the calculator cleared, entering no will exit the calculator (yes/no): ")) == "yes":
            continue_calc = False
            calculator()
        else:
            print("Calculator has been terminated")
            return 
             
calculator()
        
