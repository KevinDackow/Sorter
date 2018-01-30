import sys
import threading
import time
import random
import argparse
#simple helper function to wait a specified number of seconds
def wait(n):
    time.sleep(n)

# a helper function that will highlight the first n sorted elements green while keeping the rest red.
def print_highlighted(l, changed_one, changed_two):
    i = 1
    for x in l:
        # if x is in the right spot.
        if x == changed_one or x == changed_two:
            print '\033[39m' + str(x) + '\033[1;m'
        else:
            if x == i:
                print '\033[42m' + str(x) + '\033[1;m',
            else:
                print '\033[41m' + str(x) + '\033[1;m',
        i = i + 1

# helper for seeing if a list is sorted.
def is_sorted(l): 
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def bubble_sort(l):
    while not is_sorted(l):
        i = 0
        while i < len(l) - 1:
            if l[i] > l[i + 1]:
                orig = int(l[i])
                lower = int(l[i + 1])
                l[i + 1] = orig
                l[i] = lower
                print_highlighted(l, l[i + 1], l[i]),
            i = i + 1

def selection_sort(l):


def main():
    parser = argparse.ArgumentParser(description='Specify type of sorting.')
    parser.add_argument('-ls', dest='list_size', action='store', type=int, default=10, help='integer for the size of the list to sort.')
    parser.add_argument('-b', dest='algorithm', action='store_const', const=bubble_sort,  help='bubble sort', default=None)
    args = parser.parse_args()
    if args.list_size <= 0:
        print 'specified list size <= 0. Using default list size of 10.'
        args.list_size = 10
    lst = range(1, args.list_size + 1)
    random.shuffle(lst)
    if args.algorithm != None:
        args.algorithm(lst, args.to_print)
    else: 
        print('No specified algorithm. Using bubblesort.')
        bubble_sort(lst)
main()