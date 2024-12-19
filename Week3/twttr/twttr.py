word = input("Input: ")
short = ""

for letter in word:
    match letter.lower():
        case "a" | "e" | "i" | "o" | "u":
            short = short
        case _:
            short += letter

print(short)