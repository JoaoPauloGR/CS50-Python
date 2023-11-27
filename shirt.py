import sys
import os
from PIL import Image
from PIL import ImageOps

# expect 3 command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# check extension for each file
root1, ext1 = os.path.splitext(sys.argv[1])
root2, ext2 = os.path.splitext(sys.argv[2])
if ext1.lower() not in [".jpg",".jpeg",".png"] or ext1.lower() not in [".jpg",".jpeg",".png"]:
    sys.exit("Invalid Input")
elif ext1.lower() != ext2.lower():
    sys.exit("Input and output have different extensions")

# reads file from the second command-line argument
file_name = sys.argv[1]
try:
    file =  open(file_name, "r")
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])

# read image
image1 = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")
size = shirt.size
image1 = ImageOps.fit(image1, size)
image1.paste(shirt, shirt)
image1.save(sys.argv[2])
