def knutt_morris_pratt(text, pattern):  
  pi = [0] * len(pattern)

  j = 0
  for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
      j = pi[j - 1]
    if pattern[i] == pattern[j]:
      j += 1
    pi[i] = j
  j = 0
  for i in range(len(text)):
    while j > 0 and text[i] != pattern[j]:
      j = pi[j - 1]
    if text[i] == pattern[j]:
      j += 1
    if j == len(pattern):
      return i - len(pattern) + 1
  return -1

print(knutt_morris_pratt("ABABDABACDABABCABAB", "ABABCABAB"))