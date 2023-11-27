import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts_list = figlet.getFonts()

if len(sys.argv) == 1:
    chosen_font = random.choice(fonts_list)
    figlet.setFont(font=chosen_font)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

str_input = input("Input: ")
print("Output: ")
print(figlet.renderText(str_input))