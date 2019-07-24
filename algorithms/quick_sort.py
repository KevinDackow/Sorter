from utilities.print_highlighted import print_highlighted
from utilities.wait import wait
from utilities.is_sorted import is_sorted

def quick_sort_all(lst, wait_time):
    quick_sort(lst, 0, len(lst)-1, wait_time)
    print_highlighted(lst, None, None)

def quick_sort(lst, l, h, wait_time):
    if l < h:
        p = partition(lst, l, h, wait_time)
        quick_sort(lst, l, p-1, wait_time)
        quick_sort(lst, p+1, h, wait_time)

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def partition(lst, l, h, wait_time):
    pivot = lst[h]
    i = l
    for j in range(l, h):
        if lst[j] < pivot:
            print_highlighted(lst, i, j)
            swap(lst, i, j)
            print_highlighted(lst, i, j)
            i += 1
            wait(wait_time)
    swap(lst, i, h)
    return i 
