def binary_search(input_array, value):
    low_index = 0
    high_index = len(input_array) - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if input_array[mid_index] == value:
            return mid_index
        elif input_array[mid_index] < value:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
    return -1
