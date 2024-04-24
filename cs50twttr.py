def main():  # ask user for str input, disragrad lower or upper case
    txt = str(input("Input: "))

    (remove_vowel(txt))


def remove_vowel(str):
    j = ""
    for i in str:  # check all vowels
        if i.lower() in ["a", "e", "i", "o", "u"]:
            i = ""  # removes all vowels then output
        j += i

    return print(f"Output: {j}")


main()
