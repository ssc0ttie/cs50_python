###COMMAND-LINE ARGUMENTS
# sys - functions pertaining to the system

import sys

# argv - a varible that list all the inputs of the user before hitting enter

# print("hello, my name is", sys.argv[1])

# what will happen if the user did not type their name? - index error

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("please type your name")


# avoiding all index error
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])


# will check for errors and will exit and will not proceed to print until satisfied
# SYS.EXIT
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello, my name is", sys.argv[1])


##APIs


##requests library - automates web download
