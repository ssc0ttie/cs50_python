from pyfiglet import Figlet
import sys


fonts = Figlet().getFonts()
# print(sys.argv[2] in fonts)

if len(sys.argv) == 1:
    f = Figlet()
    i = input("Input: ")
    print(f.renderText(i))

elif len(sys.argv) == 2:
    print("Invalid usage")
    sys.exit(1)

elif len(sys.argv) == 3:

    if sys.argv[1] not in ["-f", "--font"]:
        print("Invalid usage")
        sys.exit(1)

    elif sys.argv[1] == "-f":
        if sys.argv[2] not in fonts:
            print("Invalid usage")
            sys.exit(1)

    elif sys.argv[1] == "--font":
        if sys.argv[2] not in fonts:
            print("Invalid usage")
            sys.exit(1)

    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:

        fnt = str(sys.argv[2])
        f = Figlet(font=fnt)
        i = input("Input: ")
        print(f.renderText(i))
