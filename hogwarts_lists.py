# students = ["Hermione", "Harry", "Ron"]

# # if you want to print 1 by 1, you need to use index
# print(students)

# for student in students:
#     print(student)

# # len function

# for i in range(len(students)):  # this will count the number of items inside the list
#     print(i + 1, students[i])  # prints a rank of the student

# # dict - dictionaries - allows you associates 1 value to another , {keys: values}

# students = {
#     "Harry": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=": ")


# dictionary within a list
students = [
    {"name": "Hermione", "house": "Gryffondor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffondor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffondor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]


for student in students:
    print(student["name"], student["house"], sep=": ")
