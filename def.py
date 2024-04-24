##DEF
def main():  # standard way of defining the main part of the program
    name = input("what's your name? ")
    return hello(name)


def hello(
    to="world",
):  # to - the parameter, "world" - the default value, this will also allow you to organize your code however you want and python will know how to prioritize
    print("hello,", to)


main()

#scope - refers to a variable only existing in the context in which you defined it.