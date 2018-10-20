from random import randint

def create_random_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

print([randint(0,50) for _ in range(10)])

def partition(a, low, high):
    i = low-1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i+=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1

def quicksort(a, low=0, high=None):
    if high==None:
        high=len(a) - 1
    if low<high:
        partition_index=partition(a, low, high)
        quicksort(a, low, partition_index-1)
        quicksort(a, partition_index+1, high)
    
a = create_random_array()

print("Unsorted array :", a)
quicksort(a)
print("Sorted array :", a)
