def BracketMatcher(strParam):

  # code goes here
  num_left = strParam.count('(')
  num_right = strParam.count(')')

  if num_left != num_right:
    return 0

  checker = {}
  checker['left'] = 0
  checker['right'] = 0

  for char in strParam:
    if char == '(':
      checker['left'] += 1

    elif char == ')':
      checker['left'] -= 1
      if checker['left'] < 0:
        return 0

    else:
      continue

  if (checker['left'] == 0 and checker['right'] == 0):
    return 1

  else:
    return 0

# keep this function call here 
print(BracketMatcher(input()))
