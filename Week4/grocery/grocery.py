d = {}

while True:
    try:
        word = input().upper()
    except EOFError:
        print("")
        break
    else:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

d = dict(sorted(d.items()))

for key in d:
    print(f"{d[key]} {key}")