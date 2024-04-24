# start amount due at 50 collect payment


def main():
    calc_due()


# subtract last payment to amount due
def calc_due():  # initial ask
    due = 50

    while due > 0:
        pay = int(input("Insert Coin: "))

        if pay in [25, 10, 5] and not due <= 0:
            due -= pay
            if due <= 0:
                break
            print(f"Amount Due: {due}")

        else:
            print(f"Amount Due: {due}")
            continue

    print(f"Change Owed: {abs(due)}")


# post amount due,stop until 0 and prompt change owed

main()
