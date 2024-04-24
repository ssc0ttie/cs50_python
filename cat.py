##LOOPS

# WHILE - allows you to ask a quiestion again and again to which the answer is true or false

# goal is to meow three times
i = 3
while i != 0:
    print("meow")
    i -= 1

i = 0
while i < 3:
    print("aww")
    i += 1


# FOR loops - allows you to loop through a list of items
# LIST - additional data type - contains multiple values in the same place

for i in range(3):
    print("woof")

# pythonic way #using _ for the sake of naming a variable you do not care about
for _ in range(3):
    print("woof pythonic")

# mas malupet
print("meoww\n" * 3, end="")


##LOOPS with input

while True:  # induce infinite loop
    n = int(input("what is n?"))
    if n > 0:  # will keep asking till user give positive value
        break

for _ in range(n):
    print("meow")
