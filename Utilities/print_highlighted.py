import colorama
from colorama import Fore, Back, Style
# a helper function that will highlight the first n sorted elements green while keeping the rest red.
def print_highlighted(l, changed_one, changed_two):
    i = 1
    for x in l:
        # if x is in the right spot.
        if x == changed_one or x == changed_two:
            print(Back.BLUE + " " + str(x) + " ", end='')
        else:
            if x == i:
                print(Back.GREEN + " " + str(x) + " ", end='')
            else:
                print(Back.RED + " " + str(x) + " ", end='')
        i = i + 1
    print(Style.RESET_ALL)