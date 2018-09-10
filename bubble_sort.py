# Bubble

data = [3,1,21,427,0,8,3,12,32]
swap_count = 0
for total_iter in range(len(data)-1, 0, -1):
    for step_iter in range(total_iter):
        if data[step_iter] > data[step_iter+1]:
            temp = data[step_iter]
            data[step_iter] = data[step_iter+1]
            data[step_iter+1] = temp
            swap_count = swap_count+1

# iterations -> n - 1 = 8
# comparison for each itertion -> n - 1  = 8
# time complexity = (n - 1) x (n - 1) = n^2-2n+1 = n^2 -> O(n^2)

print(swap_count)
print(data) # Sorted now

