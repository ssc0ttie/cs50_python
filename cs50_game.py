import random


while True:
    try:
        n = input("Level: ")
        if n <= 0:
            raise ValueError
    except (TypeError, ValueError):
        continue
    else:
        target = random.randrange(1, n)
        g = input("Guess: ")
        try:
            if g > n:
                print("Too large!")
            elif g < n:
                print("Too small!")
            elif g == n:
                print("Just right!")
        except TypeError:
            pass
