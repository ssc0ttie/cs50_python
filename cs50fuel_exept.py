def main():
    status = check_fuel("what is the indicator?")
    print(status)


def check_fuel(prompt):
    while True:
        try:
            fraction = input("Fraction: ")
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])
            indicator = x / y

            if indicator <= 0.01:
                return "E"
            elif 0.99 < indicator == 1:
                return "F"
            elif 1 > indicator:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return f"{str(int(round(indicator*100,0)))}%"


main()
