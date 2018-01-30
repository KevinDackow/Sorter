from Utilities.print_highlighted import print_highlighted
from Utilities.wait import wait
from Utilities.is_sorted import is_sorted

def bubble_sort(l, wait_time):
    while not is_sorted(l):
        i = 0
        while i < len(l) - 1:
            if l[i] > l[i + 1]:
                orig = int(l[i])
                lower = int(l[i + 1])
                l[i + 1] = orig
                l[i] = lower
                print_highlighted(l, l[i + 1], l[i])
                wait(wait_time)
                print('')
            i = i + 1
    print_highlighted(l, None, None)
