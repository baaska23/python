def longest_common_subsequence(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
    return 0
  else:
    if s1[-1] == s2[-1]:
      return 1 + longest_common_subsequence(s1[:-1], s2[:-1])
    else:
      return max(longest_common_subsequence(s1[:-1], s2), longest_common_subsequence(s1, s2[:-1]))

def knapsack(weights, profits, capacity):
  if len(weights) == 0 or capacity <= 0:
    return 0
  else:
    if weights[-1] > capacity:
      return knapsack(weights[:-1], profits[:-1], capacity)
    else:
      return max(profits[-1] + knapsack(weights[:-1], profits[:-1], capacity - weights[-1]), knapsack(weights[:-1], profits[:-1], capacity))    

def fibonacci_sequence(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

def add(a, b):
  return a + b

print(longest_common_subsequence("danke", "thanks"))
print(knapsack([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 6))
print(fibonacci_sequence(10))