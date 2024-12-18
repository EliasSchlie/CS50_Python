def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(" ")
    hours, minutes = time[0].split(":")
    dec = float(hours) + (float(minutes) / 60)
    if time[-1] == "p.m.":
        return (dec + 12)
    else:
        return dec


if __name__ == "__main__":
    main()