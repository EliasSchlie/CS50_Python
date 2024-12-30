def main():
    while True:
        fraction = input("Fraction: ")
        try:
            num = convert(fraction)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(gauge(num))


def convert(fraction):
    v1, v2 = fraction.split("/")
    x = (int(v1) / int(v2))
    if x <= 1:
        x = round(x * 100)
        return x
    else:
        raise ValueError("More than 100%")


def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return f"{x}%"


if __name__ == "__main__":
    main()

