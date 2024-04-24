# MODULO


def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


##BOOL - can only be True or False


def is_even(n):  # more pythonic
    return True if n % 2 == 0 else False
    # return n % 2 == 0


# yet another approach, since the question is bool there no need to add if
main()
