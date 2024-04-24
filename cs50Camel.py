def main():
    camelCase = input("camelCase:")
    print(to_snake(camelCase))


def to_snake(txt):
    word = ""
    for i in txt:
        if i.isupper():
            j = i.lower()
            i = "_"
            word += i + j
        else:
            word += i
    return word


main()
