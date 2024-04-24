def main():
    fruit = input("Item: ").title()
    print(check_calories(fruit))


def check_calories(item):

    fruits_list = [
        {"fruit": "Cantaloupe", "Calories": 50},
        {"fruit": "Honeydew", "Calories": 50},
        {"fruit": "Pineapple", "Calories": 50},
        {"fruit": "Strawberries", "Calories": 50},
        {"fruit": "Tangerine", "Calories": 50},
        {"fruit": "Grapefruit", "Calories": 60},
        {"fruit": "Nectarine", "Calories": 60},
        {"fruit": "Avocado", "Calories": 50},
        {"fruit": "Sweet Cherries", "Calories": 100},
        {"fruit": "Peach", "Calories": 60},
        {"fruit": "Plums", "Calories": 70},
        {"fruit": "Orange", "Calories": 80},
        {"fruit": "Watermelon", "Calories": 80},
        {"fruit": "Grapes", "Calories": 90},
        {"fruit": "Kiwifruit", "Calories": 90},
        {"fruit": "Pear", "Calories": 100},
        {"fruit": "Sweet", "Calories": 100},
        {"fruit": "Banana", "Calories": 110},
        {"fruit": "Apple", "Calories": 130},
    ]

    for fruit in fruits_list:
        if fruit["fruit"] == item:
            return fruit["Calories"]
    return ""


main()
