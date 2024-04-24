def main():
    generate_integer(get_level())


def get_level():
    import sys

    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                continue
            elif n > 3:
                continue
            else:
                return n

        except (ValueError, IndexError):
            pass


def generate_integer(level):
    import random

    score = 0
    mistake = 0

    for prob in range(1, 11):
        min_value = 10 ** (level - 1)  # Minimum value for n digits
        max_value = (10**level) - 1  # Maximum value for n digits

        x = random.randint(min_value, max_value)
        y = random.randint(min_value, max_value)

        try:
            while mistake < 3:
                a = int(input(f"{x} + {y} = "))
                if a != (x + y):
                    print("EEE")
                    mistake += 1

                else:
                    break

            if mistake == 3:
                print(f"{x} + {y} = {x + y}")
                mistake = 0

            elif a == (x + y):
                score += 1

        except (ValueError, TypeError):
            pass
    print("Score: " + str(score))


if __name__ == "__main__":
    main()
