import json
import os
import time
from colorama import Fore
import checker

clear = lambda: os.system('cls')
clear()


def stock(Stock):
    f = open("balance.json", "r")
    f1 = json.load(f)
    f.close()

    check = checker.sym_check_1(Stock)
    StockPrice = float(checker.StockPrice(Stock))
    if check:
        if float(f1) > StockPrice:
            clear()
            print(Fore.WHITE, "How man shares of " + str.upper(Stock) + " do you wanna buy? \n")
            quantity = input("> ")
            try:
                if float(f1) > float(StockPrice * int(quantity)):
                    clear()
                    print(Fore.WHITE, "You have bought " + quantity + " share(s) for",
                          round(StockPrice * int(quantity), 2), "$!")

                    yourStocks = {}

                    filename = 'yourStocks.json'

                    i = open('yourStocks.json', 'r')
                    i1 = json.load(i)

                    yourStocks[Stock] = int(quantity)

                    f = open("balance.json", "r")
                    f1 = json.load(f)
                    f.close()

                    with open(filename, "r+") as file:
                        if str.upper(Stock) in i1:
                            data = json.load(file)
                            data[str.upper(Stock)] += int(quantity)
                            file.seek(0)
                            json.dump(data, file)
                        else:
                            data = json.load(file)
                            data[str.upper(Stock)] = int(quantity)
                            file.seek(0)
                            json.dump(data, file)

                    f1 = float(f1) - float(StockPrice * int(quantity))
                    f = open("balance.json", "w+")
                    json.dump(round(f1, 2), f)
                    f.close()

                    time.sleep(2)
                    clear()
                else:
                    clear()
                    print("You don't have enough money, buy fewer shares!")
                    time.sleep(2)
                    clear()
            except:
                clear()
                print(Fore.WHITE, "Please enter a valid number!")
                time.sleep(2)
                clear()
        else:
            clear()
            print("You don't have enough money!")
            time.sleep(2)
            clear()
