def main():
    cost = value(input("Greeting: "))
    print(f"${cost}")


def value(greeting):
    greeting = str(greeting).strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()