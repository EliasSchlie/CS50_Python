import sys
import pyfiglet
from random import choice

i = sys.argv[1:]

if i[0] == "0" and len(i) == 1: 
    fonts = pyfiglet.FigletFont.getFonts()
    fon = choice(fonts)
    f = pyfiglet.Figlet(font=fon)
elif len(i) == 2 and (i[0] == "-f" or i[0] == "-font"): 
    try:
        f = pyfiglet.Figlet(font=i[1])
    except TypeError:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(f.renderText(text))
