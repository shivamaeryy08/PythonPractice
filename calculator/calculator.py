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

num1 = int(input("What's the first number?: "))

for key in operators:
    print(key)

symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
answer = operators[symbol](num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")
continue_calc = input("Do you want to continue using the calculator? Enter yes or no: ")
while continue_calc == "yes":
    symbol = input("Pick an operation: ")
    next_num = int(input("What's the next number?: "))
    new_answer = operators[symbol](answer, next_num)
    print(f"{answer} {symbol} {next_num} = {new_answer}")
    answer = new_answer
    continue_calc = input(
        "Do you want to continue using the calculator? Enter yes or no: "
    )
