##FUNCTIONS##

# print("hello, world")


# function - print()
# arguements -inputs from the user that u want the function to do ("what is inside here")
# side effect - your result
# bugs - mistakes


# Return Values - Variables

name = input("whats your name? ")

print("Hello", name)  # using 2 arguments

print("Hello " + name)  # using concat


# DOCUMENTATION

"""
print(*objects, sep=' ', end='\n', file=None, flush=False)

named parameters - optional
"""
print("Hello ", end="")  # removing new line
print(name)  # removing new line

print(f"hello, {name}")  # using f string
# comments

name2 = input("whats your name? ").strip().title()
print(f"hello, {name2}")

# split user's name into first name and last name

first, last = name.title().split(" ")
print(f"hello, {first}")
# use as pseudo code - like a to do list to structure what you need to do
