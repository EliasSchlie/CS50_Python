def main():
    word = str(input("Input: "))
    short_word = shorten(word)
    print(short_word)


def shorten(word):
    short = ""
    for letter in word:
        match letter.lower():
            case "a" | "e" | "i" | "o" | "u":
                short = short
            case _:
                short += letter
    return short


if __name__ == "__main__":
    main()