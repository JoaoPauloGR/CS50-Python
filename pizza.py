import sys
import csv
from tabulate import tabulate

pizza_prices = []

# expect 2 command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# try to open the specified file
file_name = sys.argv[1]
try:
    file =  open(file_name, "r")
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    # check file extension
    file_str, file_ext = file_name.rsplit(".")
    if  file_ext != "csv":
        sys.exit("Not a CSV file")

reader = csv.reader(file)
for row in reader:
    pizza_prices.append({"name": row[0], "small": row[1], "large": row[2]})
prices_grid = tabulate(pizza_prices, headers = "firstrow", tablefmt = "grid")
print(prices_grid)