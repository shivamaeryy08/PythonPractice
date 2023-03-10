def add_numbers(a=3, b=2, c=3):
    pass
    # can call with with add_numbers()
    # to modify simply only use that argument as keyword


# *args inf positional args
def add(*args):
    sum = 0
    for numbers in args:
        sum += numbers
    print(args)
    print(sum)


# each arg will be in one tuple

add(1, 2, 3)


# inf keyword args

def calculate(**kwargs):
    # will output {'add': 3, 'multiply' : 5}
    for key, value in kwargs.items():
        print(kwargs[key])


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']  # use get with dictionary if key doesnt exist to avoid errros, dict.get[key]


car = Car(make="Toyata", model="79")
