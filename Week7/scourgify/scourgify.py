import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    f_name = sys.argv[1]
    ex_name = sys.argv[2]
    if ex_name[-4:] != f_name[-4:] != ".csv":
        sys.exit("Not a CSV file")
else:
    sys.exit("Too few command-line arguments")

try:
    with open(f_name) as input:
        reader = csv.DictReader(input)
        output = []
        with open(ex_name, "w") as final:
            writer = csv.DictWriter(final, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit("File dose not exist")