from datetime import date
from sys import exit
from num2words import num2words
import inflect

p = inflect.engine()

def main():
    dat = input("Date of Birth: ")
    print(getMinTillNowInWords(getBirthday(dat)))

def getMinTillNowInWords(dat):
    days = date.today() - dat
    days = days.days * 24 * 60
    return " ".join(" ".join((p.number_to_words(days).capitalize(), "minutes")).split(" and "))

def getBirthday(dat):
    try:
        year, month, day = dat.split("-")
        birth = date(int(year), int(month), int(day))
    except ValueError:
        exit("Invalid")
    return birth


if __name__ == "__main__":
    main()