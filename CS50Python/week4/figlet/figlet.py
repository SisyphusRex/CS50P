from pyfiglet import Figlet
import random
figlet = Figlet()
import sys

def main():
    font_list = figlet.getFonts()
    if len(sys.argv) == 2:
        sys.exit("Can't have only one argument")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments.")
    if len(sys.argv) == 1:
        my_font = random.choice(font_list)
        figlet.setFont(font=my_font)
        my_input = input("Input: ")
        print(figlet.renderText(my_input))
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print(sys.argv[1])
            sys.exit("-f or --font required")
        if sys.argv[2] not in font_list:
            sys.exit("Name an actual font.")
        my_font = sys.argv[2]
        figlet.setFont(font=my_font)
        my_input = input("Input: ")
        print(figlet.renderText(my_input))

if __name__ == "__main__":
    main()

