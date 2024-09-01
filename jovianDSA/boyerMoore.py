def boyer_moore(text, pattern):
  """
  Performs Boyer-Moore string search on the given text for the pattern.

  Args:
      text: The text string to search in.
      pattern: The pattern string to search for.

  Returns:
      The starting index of the first occurrence of the pattern in the text, 
      or -1 if not found.
  """
  # Build bad character table
  bad_char_table = build_bad_char_table(pattern)

  # Lengths of text and pattern
  n = len(text)
  m = len(pattern)

  # Start index for pattern matching
  i = m - 1

  while i <= n - m:
    # Check for pattern match
    j = m - 1
    while j >= 0 and text[i - j] == pattern[j]:
      j -= 1

    # Pattern match found
    if j == -1:
      return i - m + 1

    # Shift the pattern based on bad character rule
    shift_bad_char = bad_char_table.get(text[i], m)

    # Good suffix rule might suggest smaller shift
    shift_good_suffix = m - 1
    for k in range(j, -1, -1):
      if pattern[k] == text[i - k]:
        shift_good_suffix = min(shift_good_suffix, m - 1 - k)
      else:
        break

    # Use the larger shift
    shift = max(shift_bad_char, shift_good_suffix)

    # Shift the pattern
    i += shift

  # Pattern not found
  return -1

def build_bad_char_table(pattern):
  """
  Builds the bad character heuristic table for the pattern.

  Args:
      pattern: The pattern string to build the table for.

  Returns:
      A dictionary where the key is a character and the value is the 
      maximum distance between the character and its last occurrence 
      in the pattern.
  """
  table = {}
  for i in range(len(pattern) - 1):
    table[pattern[i]] = len(pattern) - i - 1
  return table

# Example usage
text = "THIS IS A TEST TEXT"
pattern = "TEST"
index = boyer_moore(text, pattern)

if index != -1:
  print("Pattern found at index:", index)
else:
  print("Pattern not found")
