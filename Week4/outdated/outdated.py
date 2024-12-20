months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            converter(input("Date: "))
            break
        except ValueError:
            pass


def converter(date):
    if "/" in date:
        date = date.split("/")
        month = int(date[0])
        day = int(date[1])
        if 0 < month < 13 and 0 < day < 32:  
            print(f"{int(date[2])}-{month:02}-{day:02}")
        else:
            int("Throw error")
    else:
        date = date.split(",")
        month, day = date[0].split(" ")
        month_num = months.index(month)
        month_num = int(month_num) + 1
        if 0 < month_num < 13 and 0 < int(day) < 32:  
            print(f"{date[1].strip()}-{month_num:02}-{int(day):02}")
        else:
            int("Throw error")

main()