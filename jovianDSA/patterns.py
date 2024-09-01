# linearDS, subset, condition
def sliding_window(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(k):
        max_sum += arr[i]
    window_sum = max_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

def subset(arr):
  n = len(arr)
  for i in range(1 << n):
    for j in range(n):
      if i & (1 << j):
        print(arr[j], end=" ")
    print

def modified_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def top_k_elements(arr, k):
    return sorted(arr, reverse=True)[:k]

def kth_largest_element(arr, k):
    return sorted(arr, reverse=True)[k - 1]

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

def topologicalSortUtil(v, adj, visited, stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)
    stack.append(v)

def topologicalSort(adj, V):
    stack = []
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    print("Topological sorting of the graph:", end=" ")
    while stack:
        print(stack.pop(), end=" ")

def two_pointers(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

print(sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(subset([1, 2, 3]))
print(modified_binary_search([1, 3, 5, 6], 1))
print(top_k_elements([1, 3, 5, 6], 3))
print(kth_largest_element([1, 3, 5, 6], 3))
print(dfs(set(), {0: [1, 2], 1: [3], 2: [3, 4], 3: [], 4: []}, 0))
print(bfs({0: [1, 2], 1: [3], 2: [3, 4], 3: [], 4: []}, 0))
print(topologicalSort({0: [1], 1: [2], 2: [3], 3: []}, 4))
print(two_pointers([1, 3, 5, 6], 14))
