import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first, last = s.split(" to ")
    return usToNormalTime(first) + " to " + usToNormalTime(last)


def usToNormalTime(time):
    if time.find(":") > 0:
        colon = time.find(":")
        hour = int(time[0:colon])
        minute = int(time[colon+1:colon+3])
    else:
        hour = int(time[0:time.find(" ")])
        minute = 0
    if hour > 12 or minute >= 60:
        raise ValueError
    if time.find("PM") > 0:
        if hour != 12:
            hour += 12
    elif hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()