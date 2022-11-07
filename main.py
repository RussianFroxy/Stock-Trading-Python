import os
import sys
import time
from colorama import Fore
import choices

# script.start
print("Load Simulation..")
time.sleep(2)
clear = lambda: os.system('cls')
clear()

while True:

    print(Fore.GREEN, "Stock Simulator\n by Artur Schlee")
    print("")
    print(Fore.WHITE, "1 -> Invest\n 2 -> Available Stocks\n 3 -> Sell\n 4 -> Your Stocks\n 5 -> Balance")
    choice = input("> ")

    if choice == "1":
        choices.choiceOne()

    elif choice == "2":
        choices.choiceTwo()

    elif choice == "3":
        choices.choiceThree()

    elif choice == "4":
        choices.choiceFour()

    elif choice == "5":
        choices.choiceFive()

    elif str.upper(choice) == "EXIT":
        sys.exit()

    else:
        clear()
        print("Please enter a valid number!")
        time.sleep(2)
        clear()
