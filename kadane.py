def kadaneAlgorithm(arr):
    current_max = arr[0]
    global_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(current_max, global_max)
    return global_max
result = kadaneAlgorithm([-2324, 42, 2342,1, -234])
print(result)   