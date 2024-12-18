camel = input("Camel case: ")
word = ""

for letter in camel:
    if letter.isupper():
        letter = "_" + letter.lower()
    word += letter

print(word)