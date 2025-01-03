import sys
import csv
from PIL import Image, ImageOps




if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    before = sys.argv[1]
    after = sys.argv[2]
    if after[-4:] == before[-4:] in (".jpg", ".png", ".gif"):
        pass
    else:
        sys.exit("Not a CSV file")
else:
    sys.exit("Too few command-line arguments")



try:
    shirt = Image.open("shirt.png")
    muppet = Image.open(before)
    muppet = ImageOps.fit(muppet, shirt.size)
    muppet.paste(shirt, mask=shirt)
    muppet.save(after)

except FileNotFoundError:
    sys.exit("File dose not exist")