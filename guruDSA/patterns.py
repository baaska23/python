def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        if target > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]

def printFunction(arr):
    return arr

ex = printFunction([1,2,3,4])
examples1 = two_pointers([-1, 0, 3, 5, 9, 12], 9)
print(examples1) # Expected output: [0, 3]
print(ex) # Expected output: [1, 2, 3, 4]
#https://www.designgurus.io/blog/grokking-the-coding-interview-patterns