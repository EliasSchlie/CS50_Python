import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip:str) -> bool: # Returns true if ip is valid IPv4 address
    if not re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", ip):
        return False
    nums = ip.split(".")
    for num in nums:
        if 0 > int(num) or int(num) > 255:
            return False
    return True



if __name__ == "__main__":
    main()
