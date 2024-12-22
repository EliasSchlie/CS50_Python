from random import randint
import sys

def main():
    level = get_int("Level: ")
    game(level)

def get_int(message):
    i = -1
    while True:
        if check_int(i):
            return int(i)
        else:
            i = input(message)

def game(level):
    res = int(randint(1, level))
    while True:
        guess = get_int("Guess: ")
        if guess > res:
            print("Too large!")
        elif guess < res:
            print("Too small!")
        else:
            sys.exit("Just right!")
        



def check_int(i):
    try:
        if int(i) > 0:
            return True
        else:
            return False
    except ValueError: 
        return False
        



main()