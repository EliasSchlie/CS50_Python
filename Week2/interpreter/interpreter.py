calc = input("Expression: ")

calc = calc.split(" ")
x = float(calc[0])
y = calc[1]
z = float(calc[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
else:
    print(x / z)
