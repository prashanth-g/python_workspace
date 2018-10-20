#with 3 arrays

from random import randint

def quicksort(input_array):
    if len(input_array)<=1 : return input_array
    smaller, equal, larger = [], [], []
    pivot = input_array[randint(0, len(input_array)-1)]

    for x in input_array:
        if x<pivot: smaller.append(x)
        elif x==pivot: equal.append(x)
        else: larger.append(x)
    
    return quicksort(smaller)+equal+quicksort(larger)

a = [10, 23, 3, 8, 44, 13]

print(quicksort(a))