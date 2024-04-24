# modules = libraries you can re use

# RANDOM Lib

# keyword = import

## random.choice(seq)

##CODE = generate.py

import random as rand

toss = rand.choice(["heads", "tails"])

print(toss)

# randint

number = rand.randint(1, 90)
print(number)

# shuffles
cards = ["jack", "queen", "king"]
rand.shuffle(cards)
for card in cards:
    print(card)

# keyword FROM


from random import choice  # loads only the choice function

coin = choice(range(1, 10))
print(coin)


##STATITICS library

import statistics as st

score = st.mean([8, 9, 10, 13, 4, 4, 5])

print(score)
