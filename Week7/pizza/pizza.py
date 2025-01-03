import sys
import tabulate
import csv

arg = sys.argv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    f_name = sys.argv[1]
    if f_name[-4:] != ".csv":
        sys.exit("Not a CSV file")
else:
    sys.exit("Too few command-line arguments")

try:
    with open(f_name) as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers="keys", tablefmt= "grid"))
except FileNotFoundError:
    sys.exit("File dose not exist")
