import sys
import csv

# expect 3 command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# reads file from the second command-line argument
file_name = sys.argv[1]
try:
    file =  open(file_name, "r")
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
else:
    # check file extension
    file_str, file_ext = file_name.rsplit(".")
    if  file_ext != "csv":
        sys.exit("Not a CSV file")

# read the csv file and split the name column into first and last name
scourgify_list = []
reader = csv.DictReader(file)
for row in reader:
    last, first = row["name"].split(",")
    scourgify_list.append({"first": first.lstrip(), "last": last.lstrip(), "house": row["house"]})

# close current file
file.close()

# get output file name from the command-line argument
output_filename = sys.argv[2]

# write in the new file in the specified format
with open(output_filename, "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for row in scourgify_list:
        writer.writerow(row)
