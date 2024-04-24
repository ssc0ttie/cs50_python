def main():
    print(order_calculator())


def order_calculator():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    bill = 0
    try:
        while True:

            # order prompt comes first
            order = str(input("Item: ").title())

            for item in menu:

                if item == order:
                    bill += float(menu[order])

                    # second order prompt comes first

            # total prompt will come after the first order
            format_bill = format(bill, ".2f")
            print(f"Total: ${format_bill}")
            continue

    except (ValueError, ZeroDivisionError):
        pass
    except EOFError:
        return bill


main()
