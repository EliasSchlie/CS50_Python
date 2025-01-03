import sys

# Error checking
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    f_name = sys.argv[1]
    if f_name[-3:] != ".py":
        sys.exit("Not a Python file")
else:
    sys.exit("Too few command-line arguments")

## Counting lines


try: 
    with open(f_name) as file:
        file = file.read()
        # Remove comments
        n_file = ""
        for line in file.split("\n"):
            if "#" in line:
                line = line[:line.find("#")]
            n_file += line + "\n"
        file = "".join(n_file)

        # Remove docstrings - I can't figgure out how 
        for doctype in (("'''", '"""')):
            parts = file.split(doctype)
            new = []
            for i in range(len(parts)):
                if i % 2 == 0 and parts[i].strip().endswith(":"):
                    new.append(parts[i]) 
                elif i % 2 == 0:
                    new.append(parts[i])
                    try:
                        new.append(parts[i+1])
                    except IndexError:
                        pass
            file = doctype.join(new)

        # Remove empty lines
        n_file = ""
        for line in file.split("\n"):
            if line.strip():
                n_file += line + "\n"
        file = n_file
        print(len(file.split("\n")) - 1)
except FileNotFoundError:
    sys.exit("File dose not exist")

