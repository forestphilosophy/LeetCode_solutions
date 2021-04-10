def find_happy_number(num):

  seen = set()

  while True:

    if num == 1:
      return True

    squared_nums_list = [(int(number))**2 for number in str(num)]

    sum_of_nums = sum(squared_nums_list)

    if sum_of_nums in seen:
      break
    else:
      seen.add(sum_of_nums)

    num = sum_of_nums
  return False
