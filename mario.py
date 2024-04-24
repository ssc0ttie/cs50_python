# #vertical column
# def main():
#     print_column(3)


# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

##printing a 3x3 brick


def main():
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):
        # print brick (#) in row
        for j in range(size):
            # print a brick (#)
            print("#", end="")
        print()  # prints a new line


main()


def main_2():
    print_square_2(5)


def print_square_2(size):
    for i in range(size):
        print("#" * size)


main_2()
