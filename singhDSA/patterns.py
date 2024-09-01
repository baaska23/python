def prefixSum(arr):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

def twoPointers(arr, i, j):
    n = len(arr)
    while i < n and j < n:
        if arr[i] == arr[j]:
            return True
        elif arr[i] < arr[j]:
            j += 1
        else:
            i += 1
    return False

def slidingWindow(arr, k):
    n = len(arr)
    if n < k:
        return -1
    windowSum = sum(arr[:k])
    maxSum = windowSum
    for i in range(1, n-k+1):
        windowSum = windowSum - arr[i-1] + arr[i+k-1]
        maxSum = max(maxSum, windowSum)
    return maxSum

def fastSlowPointers(arr):
    slow = arr[0]
    fast = arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

def linkedListInPlaceReversal(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def monotonicStack(arr):
    n = len(arr)
    stack = []
    result = [0]*n
    for i in range(n-1, -1, -1):
        while stack and arr[i] > arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)
    return result

def topKElements(arr, k):
    pass

def overlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

def modifiedBinarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binaryTreeTraversal(root):
    if root is None:
        return []
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def dfs(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

def bfs(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

def matrixTraversal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    row, col = 0, 0
    while row < m and col < n:
        for i in range(col, n):
            result.append(matrix[row][i])
        row += 1
        for i in range(row, m):
            result.append(matrix[i][n-1])
        n -= 1
        if row < m:
            for i in range(n-1, col-1, -1):
                result.append(matrix[m-1][i])
            m -= 1
        if col < n:
            for i in range(m-1, row-1, -1):
                result.append(matrix[i][col])
            col += 1
    return result

def backtracking(arr):
    result = []
    def backtrack(path, start):
        result.append(path)
        for i in range(start, len(arr)):
            backtrack(path + [arr[i]], i+1)
    backtrack([], 0)
    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]

def longestCommonSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def longestIncreasingSubsequence(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def subsetSum(arr, target):
    n = len(arr)
    dp = [[False]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

def matrixChainMultiplication(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n):
        for i in range(1, n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])
    return dp[1][n-1]

def kadanesAlgorithm(arr):
    n = len(arr)
    maxSum = arr[0]
    currentSum = arr[0]
    for i in range(1, n):
        currentSum = max(arr[i], currentSum + arr[i])
        maxSum = max(maxSum, currentSum)
    return maxSum

def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

def unboundedKnapsack(weights, values, capacity):
    n = len(weights)
    dp = [0]*(capacity+1)
    for i in range(1, capacity+1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], values[j] + dp[i-weights[j]])
    return dp[capacity]

def longestPalindromicSubstring(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start = 0
    maxLength = 1
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
            if dp[i][j] and length > maxLength:
                start = i
                maxLength = length
    return s[start:start+maxLength]

def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def stringPartition(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    result = []
    def backtrack(start, path):
        if start == n:
            result.append(path)
            return
        for i in range(start, n):
            if dp[start][i]:
                backtrack(i+1, path + [s[start:i+1]])
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 1:
                dp[i][j] = True
            elif length == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
    backtrack(0, [])
    return result

def catalanNumbers(n):
    dp = [1]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

def countDistinctWays(arr, target):
    n = len(arr)
    dp = [[0]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

def stateMachineDP(arr):
    n = len(arr)
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -arr[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - arr[i])
    return dp[n-1][0]

