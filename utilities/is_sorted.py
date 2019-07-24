# helper for seeing if a list is sorted.
def is_sorted(l): 
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

