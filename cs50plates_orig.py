def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not start_with_two_letters(s):
        return False
    if not min_two_max_six_char(s):
        return False
    if num_mid_plate(s):
        return False
    if first_num_not_zero(s):
        return False
    if not special_char(s):
        return False
    if not char_in_the_end(s):
        return False

    return True


def min_two_max_six_char(s):
    return 2 <= len(s) <= 6


def start_with_two_letters(s):
    return s[:2].isalpha()


def first_num_not_zero(s):
    dig = ""
    for i in s:
        if i.isdigit():
            dig += i
    # return int(dig[0]) == 0
    return len(dig) > 0 and int(dig[0]) == 0


def num_mid_plate(s):
    return s[-1].isalpha()


def special_char(s):
    return "." not in s and "!" not in s and " " not in s


def char_in_the_end(s):
    return s[-2:].isdigit()


main()
