from utilities.print_highlighted import print_highlighted
from utilities.is_sorted import is_sorted
from utilities.wait import wait
import random

def bogo_sort(l, wait_time):
    while not is_sorted(l):
        random.shuffle(l)
        print_highlighted(l, None, None)
        wait(wait_time)
