import random


def main():
    level = get_level()
    score = 0
    for _ in range(1, 11):
        a = generate_integer(level)
        b = generate_integer(level)
        result = a + b
        for out in ["EEE", "EEE", f"{a} + {b} = {result}"]:
            i = input(f"{a} + {b} = ")
            if i == str(result):
                score += 1
                break
            else:
                print(out)
    print(f"Score: {score}")



def get_level():
    level = 0
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4: 
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    high = 10 ** level - 1
    low = 10 ** (level - 1)
    return random.randint(low, high)


if __name__ == "__main__":
    main()