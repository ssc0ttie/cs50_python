x = int(input("what is x? "))
y = int(input("what is y? "))

# this CONTROL FLOW in programming
# regardless the answer is true or false it will still proceed with the next question
# MUTUALLY EXCLUSIVE

if x < y:
    print("x is less than y")
if x > y:
    print("y is less than x")
if x == y:
    print("y is equal to x")


##WILL STOP ONCE TRUE -> MUTUALLY EXCLUSIVE
if x < y:
    print("x is less than y")
elif x > y:
    print("y is less than x")
elif x == y:
    print("y is equal to x")


##same result, but less complex, its easier to understand and less work for the program
if x < y:
    print("x is less than y")
elif x > y:
    print("y is less than x")
else:
    print("y is equal to x")

# OR

if x < y or x > y:
    print("x is not equal to y")
else:
    print("y is equal to x")
