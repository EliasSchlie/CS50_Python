while True:
    fraction = input("Fraction: ")
    try:
        v1, v2 = fraction.split("/")
        x = (int(v1) / int(v2))
        if x <= 1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if x >= 0.99:
    print("F")
elif x <= 0.01:
    print("E")
else:
    x = round(x * 100)
    print(f"{x}%")