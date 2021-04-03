def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
  result = []
  window_start = 0
  window_end = k

  for i in range(len(str) - k):

    while len(set(str[window_start:window_end])) <= k and window_end < len(str):
      result.append(len(str[window_start:window_end]))
      window_end += 1
      
    window_start += 1

  return max(result)
