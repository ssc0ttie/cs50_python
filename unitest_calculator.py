def main():
    x = int(input("what is x?"))
    print("x squared is", square(x))


def square(n):
    return n + n


if (
    __name__ == "__main__"
):  # making sure main() is not always called when used as a module
    main()
