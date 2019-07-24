import sys
import threading
import random
import argparse
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bogo_sort import bogo_sort
from algorithms.quick_sort import quick_sort_all

def main():
    parser = argparse.ArgumentParser(description='Specify type of sorting.')
    parser.add_argument('-ls', dest='list_size', action='store', type=int, default=10, help='integer for the size of the list to sort.')
    parser.add_argument('-wt', dest='wait_time', action='store', type=float, default=0, help='integer corresponding to time between prints.')
    parser.add_argument('-b', dest='algorithm', action='store_const', const=bubble_sort,  help='bubble sort', default=None)
    parser.add_argument('-i', dest='algorithm', action='store_const', const=insertion_sort,  help='insertion sort', default=None)
    parser.add_argument('-bogo', dest='algorithm', action='store_const', const=bogo_sort,  help='bogo sort', default=None)
    parser.add_argument('-q', dest='algorithm', action='store_const', const=quick_sort_all,  help='quick sort', default=None)
    args = parser.parse_args()
    if args.list_size <= 0:
        print('specified list size <= 0. Using default list size of 10.')
        args.list_size = 10
    lst = list(range(1, args.list_size + 1))
    random.shuffle(lst)
    if args.algorithm != None:
        args.algorithm(lst, args.wait_time)
    else: 
        print('No specified algorithm. Using bubblesort.')
        bubble_sort(lst, args.wait_time)

main()
