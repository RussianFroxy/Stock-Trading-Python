import json
import os
import time
from colorama import Fore
import checker

clear = lambda: os.system('cls')
clear()


def sellStock(Stock):
    filename = 'yourStocks.json'

    i = open('yourStocks.json', 'r')
    i1 = json.load(i)

    with open(filename, "r+") as file:
        if str.upper(Stock) in i1:
            clear()
            print(Fore.WHITE, "How many shares of ", str.upper(Stock), " do you wanna sell?\n")
            quantity = input("> ")

            try:
                int(quantity)
            except:
                clear()
                print(Fore.WHITE, "Please enter a valid number!")
                clear()

            if i1[str.upper(Stock)] < int(quantity):
                clear()
                print(Fore.WHITE, "You don't have that many shares of", str.upper(Stock), "!")
                time.sleep(2)
                clear()

            else:
                AktienPreis = float(checker.StockPrice(Stock))

                with open(filename, "r+") as file:
                    data = json.load(file)
                    data[str.upper(Stock)] = data[str.upper(Stock)] - int(quantity)
                    file.seek(0)
                    json.dump(data, file)

                    if data[str.upper(Stock)] == 0:
                        del data[str.upper(Stock)]
                        dictStocks = data
                        file.truncate(0)
                        file.seek(0)
                        json.dump(dictStocks, file)

                f = open("balance.json", "r")
                f1 = json.load(f)
                f.close()

                f1 = float(f1) + (float(AktienPreis * int(quantity)))
                f = open("balance.json", "w+")
                json.dump(round(f1, 2), f)
                f.close()

                clear()
                print(Fore.WHITE, "You have sold ", quantity, " share(s) of ", str.upper(Stock), " for ",
                      round(AktienPreis * int(quantity), 2), "$!")
                time.sleep(2)
                clear()
        else:
            clear()
            print(Fore.WHITE, "You don't own that Stock!")
            time.sleep(2)
            clear()
