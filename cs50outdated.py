def parse():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:
            d = str(input("Date: ")).strip()

            if " " in d and "," in d:
                mm, dd = d.split(" ", maxsplit=1)
                yy = dd.split(",")[1].strip()
                dd = dd.split(",")[0].strip()

                mm = months.index(mm) + 1

            elif " " in d and "," not in d:
                raise ValueError

            elif "/" in d:
                mm, dd, yy = d.split("/", maxsplit=2)
            elif "," in d:
                mm, dd, yy = d.split(",", maxsplit=2)

            if int(mm) < 1 or int(mm) > 12:
                raise ValueError
            if int(dd) < 1 or int(dd) > 31:
                raise ValueError

        except ValueError:
            continue

        return print(f"{yy}-{int(mm):02}-{int(dd):02}")


parse()
