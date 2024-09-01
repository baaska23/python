def slidingWindow(arr, k):
    current_sum = sum(arr[:k])
    global_sum = current_sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        global_sum = max(current_sum, global_sum)
    return global_sum

result = slidingWindow([-2324, 42, 200,100, -234], 3)


def hahha(arr, k):
    current_sum = sum(arr[:k])
    return current_sum
result = hahha([-200, 100, 200,100, -234], 2)
print(result)