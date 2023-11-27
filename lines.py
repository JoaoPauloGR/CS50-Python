import sys

# expect 2 command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# reads file from the second command-line argument
line_counter = 0
file_name = sys.argv[1]
try:
    file =  open(file_name, "r")
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    # check file extension
    file_str, file_ext = file_name.rsplit(".")
    if  file_ext != "py":
        sys.exit("Not a Python file")
    for line in file:
        # if line is blank, ignore it
        if line.isspace():
            pass
         # if line is a comment, ignore it
        elif line.lstrip()[0] == "#":
            pass
        # any case else, adds to the line counter
        else:
            line_counter += 1

print(line_counter)