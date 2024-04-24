name = input("whats your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# else:
#     print("Who?")


match name:
    case "Harry" | "Hermione" | "Ron":  # pipe will indicate "OR"
        print("gryffindor")
    case "Draco":
        print("Slytherin")
    case (
        _
    ):  # underscore will handle anythong else other than what we specify - "catch all"
        print("Who?")
