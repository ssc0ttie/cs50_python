import inflect

# ask user for items
# store in a list
names = []
try:
    while True:
        # order prompt comes first
        name = str(input("Name: "))
        names.append(name)
except EOFError:
    pass

    p = inflect.engine()
    ad = "Adieu, adieu, to "

    print(ad, p.join(names))
