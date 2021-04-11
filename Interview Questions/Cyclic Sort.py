def cyclic_sort(nums):
  # TODO: Write your code here
  cur = 0
  while cur < len(nums):
    while nums[cur] != cur + 1:
      index1 = nums[cur] - 1
      index2 = cur 
      nums[index1], nums[index2] = nums[index2], nums[index1]
      
    cur += 1
    continue

  return nums
