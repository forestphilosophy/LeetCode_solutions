class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        #Extract all the list items
        list_items = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                list_items.append(nums[i][j])
        #Group the list items into the specified columns 
        ans = [list_items[i:i+c] for i in range(0, len(list_items), c)]
        
        if len(ans) == r:
            return ans
        else:
            return nums
