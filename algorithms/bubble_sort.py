from utilities.print_highlighted import print_highlighted
from utilities.wait import wait
from utilities.is_sorted import is_sorted

def bubble_sort(l, wait_time):
    has_bubbled = True
    i = 0
    while has_bubbled:
        has_bubbled = False
        while i < len(l) - 1:
            if l[i] > l[i + 1]:
                has_bubbled = True
                orig = int(l[i])
                lower = int(l[i + 1])
                l[i + 1] = orig
                l[i] = lower
                print_highlighted(l, l[i + 1], l[i])
                wait(wait_time)
                print('')
            i = i + 1
    print_highlighted(l, None, None)
