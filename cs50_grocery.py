def main():
    summarize_basket(collect_items())


def collect_items():
    # ask user for items
    # store in a list
    list = []
    try:
        while True:
            # order prompt comes first
            item = str(input())
            list.append(item)

    except (ValueError, ZeroDivisionError, EOFError):
        pass
    except EOFError:
        pass
    return list


# loop input prompt


# summarize list to uppercase, sorted alphabetical, prefix with total input per item
def summarize_basket(grocery):
    # items collected via user input
    # grocery = ["scott","odc","pia","jeck","glads", "scott"]
    counter = {}

    # count the occurence of the items, will result to a dictionary of the count of values
    for item in grocery:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1

    # sort alpabetical the dictionary
    sorted_counter = dict(sorted(counter.items()))

    # finding the highest count

    for item, count in sorted_counter.items():
        print(count, item.upper())


main()
