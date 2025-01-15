import validators

mail = input("What is your e-mail? ")
if validators.email(mail):
    print("Valid")
else:
    print("Invalid")
