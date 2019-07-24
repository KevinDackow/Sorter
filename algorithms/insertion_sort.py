from utilities.print_highlighted import print_highlighted
from utilities.wait import wait
from utilities.is_sorted import is_sorted

def insertion_sort(l, wait_time):
    for i in range(1, len(l)):
        value = l[i]
        index = i - 1
        while index >= 0:
            if value < l[index]:
                l[index + 1] = l[index]
                l[index] = value
                index = index - 1
                print_highlighted(l, l[index + 1], l[index])
            else:
                break
            wait(wait_time)
    print_highlighted(l, None, None)
