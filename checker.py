import json
import os
import time
import requests
from colorama import Fore

clear = lambda: os.system('cls')
clear()

HEADER = {'User-agent': 'Mozilla/5.0'}


def sym_check_1(symbol_in):
    try:
        symbol = symbol_in
        response = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}", headers=HEADER)
        data = response.text
        parse_json = json.loads(data)
        global PRICE_EUR
        PRICE_EUR = round(parse_json['chart']['result'][0]['meta']['regularMarketPrice'], 2)
        status = response.status_code
        if status == 200:
            return True
    except:
        print("")
        print(Fore.WHITE, "Sorry, this stock is not available!")
        time.sleep(2)
        clear()


def sym_check_2(symbol_in):
    try:
        symbol = symbol_in
        response = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}", headers=HEADER)
        data = response.text
        parse_json = json.loads(data)
        PRICE_EUR = round(parse_json['chart']['result'][0]['meta']['regularMarketPrice'], 2)
        status = response.status_code
        if status == 200:
            print("")
            print(Fore.WHITE, "You can buy this Stock for " + str(PRICE_EUR) + "$!")
            time.sleep(2)
            clear()
    except:
        print("")
        print(Fore.WHITE, "Sorry, this stock is not available!")
        time.sleep(2)
        clear()


def StockPrice(symbol_in):
    try:
        symbol = symbol_in
        response = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}", headers=HEADER)
        data = response.text
        parse_json = json.loads(data)
        PRICE_EUR = round(parse_json['chart']['result'][0]['meta']['regularMarketPrice'], 2)
        return PRICE_EUR
    except:
        clear()
