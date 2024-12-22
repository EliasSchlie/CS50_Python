names = []

while True:
    try:
        names += [input("Name: ")]
    except EOFError:
        print("Adieu, adieu, to ", end = "")
        if len(names) > 2:
            for name in names[:-1]:
                print(name + ", ", end = "")
            print("and ", end = "")
        elif len(names) == 2:
            print(f"{names[-2]} and ", end = "")
        print(names[-1])
        break
