def main():
    # prompt user for data
    date = input("Date: ")
    parse(date)


def parse(d):
    while True:
        try:

            if " " in d:
                mm, dd = d.split(" ", maxsplit=1)
                yy = dd.split(",")[1].strip()
                dd = dd.split(",")[0].strip()
            elif "/" in d:
                mm, dd, yy = d.split("/", maxsplit=2)
            elif "," in d:
                mm, dd, yy = d.split(",", maxsplit=2)

            if mm < 1 or mm > 12:
                raise ValueError
            if dd < 1 or dd > 31:
                raise ValueError

        except ValueError:
            pass

        return print(f"{yy} - {dd:02} - {mm:02}")


main()
