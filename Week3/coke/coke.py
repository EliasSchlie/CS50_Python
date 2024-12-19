cost = int(50)

while True:
    print("Amount Due: " + str(cost))
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        cost = cost - coin
        if cost <= 0:
            print("Change Owed: " + str(-cost))
            break
    else:
        print("Invalid Coin")

