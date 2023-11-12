import json
import os
import time
from colorama import Fore
import checker
import buy
import sell

clear = lambda: os.system('cls')


def choiceOne():
    clear()
    print(Fore.LIGHTBLACK_EX, "Options: \n 1 -> Back \n 2 -> Available Stocks")
    print(" ")
    print(Fore.WHITE, "Please enter Stock-Symbol: \n")
    choice = str.lower(input("> "))

    if choice == "1":
        clear()

    elif choice == "2":
        choiceTwo()
        clear()

    else:
        buy.stock(choice)


def choiceTwo():
    clear()
    print(Fore.LIGHTBLACK_EX, "Options: \n 1 -> Back")
    print(" ")
    print(Fore.WHITE, "Please enter Stock-Symbol: \n")
    choice = input("> ")

    if choice == "1":
        clear()
    else:
        checker.sym_check_2(choice)


def choiceThree():
    clear()
    print(Fore.LIGHTBLACK_EX, "Options: \n 1 -> Back \n")

    i = open('yourStocks.json', 'r')

    with open('yourStocks.json', "r+") as file:
        if not bool(json.load(i)):
            print(Fore.WHITE, "You haven't bought Stocks yet!")
            print(" ")
            choice = input("> ")

            if choice == "1":
                clear()
        else:
            i = open('yourStocks.json', 'r')

            for x, y in json.load(i).items():
                print(Fore.WHITE, "->", x + ":", y)

            choice = input("> ")

            if choice == "1":
                clear()

            else:
                sell.sellStock(choice)


def choiceFour():
    clear()
    print(Fore.LIGHTBLACK_EX, "Options: \n 1 -> Back \n")

    i = open('yourStocks.json', 'r')

    with open('yourStocks.json', "r+") as file:
        if not bool(json.load(i)):
            print(Fore.WHITE, "You haven't bought Stocks yet!")
            print(" ")
            choice = input("> ")

            if choice == "1":
                clear()
        else:
            i = open('yourStocks.json', 'r')

            for x, y in json.load(i).items():
                print(Fore.WHITE, x + ":", y)

            # print(" ")
            choice = input("> ")

            if choice == "1":
                clear()


def choiceFive():
    clear()
    f = open('balance.json')
    f1 = json.load(f)
    b = f1
    print(Fore.LIGHTBLACK_EX, "Options: \n 1 -> Back")
    print(" ")
    print(Fore.WHITE, "Balance: " + str(b) + "$")
    print(" ")
    choice = input("> ")

    if choice == "1":
        clear()
