def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 > len(s) or len(s) > 6:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    condition = True
    for letter in s:
        if condition and letter.isalpha():
            condition = True
        elif condition and letter == "0":
            return False
        elif letter.isdigit():
            condition = False
        else:
            return False
    return True

if __name__ == "__main__":
    main()