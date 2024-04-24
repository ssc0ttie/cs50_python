# print ("hello, world)

# #syntaxerror - you must fix yourself

# #run time error - errors from user inputs

# x = int(input("what is x?"))
# print(f"x is {x}")

# #what if user input string?

# #VALUEERROR - error from value user gave

# #defensive programming

# #TRY , EXCEPT

# try:
#     x = int(input("what is x?"))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# #best practice is to catch the specific error and not to cast a blanket for all trype of error

# #NAMEERROR - refere to your code, you're doing something that you shouldn't

# #try and exept supports ELSE
# try:
#     y = int(input("what is y?"))
# except ValueError:
#     print("y is not an integer")
# else:
#     print(f"x is {y}")

# you can loop until the users cooperate and not exit the program


def main():
    y = get_int()
    print(f"x is {y}")


def get_int():
    while True:  # breaks the loop when the user enters correct input
        try:
            y = int(input("what is y?"))
        except ValueError:
            pass  # PASS silently ignore the error - this will not prompt the error message
            # print("y is not an integer") # original error message
        else:
            # break
            return y  # return will allow you to break and return the value


# PASS silently ignore the error - this will not prompt the error message
main()


##you could do IF (conditionals) statements to test if the input is int. But the pythonic way is to TRY something , hope it works and makesure you are handling the error


"""
a more reusable code
"""


def main():
    y = get_int("what's y?")  # passing a parameter
    print(f"y is {y}")


def get_int(prompt):  # call your parameter whatever
    while True:  # breaks the loop when the user enters correct input
        try:
            y = int(input(prompt))
        except ValueError:
            pass  # PASS silently ignore the error - this will not prompt the error message
            # print("y is not an integer") # original error message
        else:
            # break
            return y  # return will allow you to break and return the value


##RAISE
