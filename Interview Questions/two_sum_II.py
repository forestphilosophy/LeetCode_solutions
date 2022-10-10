class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = len(nums) - 1
        
        heap_map = [[idx,val] for idx,val in enumerate(nums)]

        while pointer_1 < pointer_2:
            
            num1 = heap_map[pointer_1][1]
            num2 = heap_map[pointer_2][1]
            
            if num1 + num2 == target:
                return [heap_map[pointer_1][0] + 1, heap_map[pointer_2][0] + 1]
            
            elif num1 + num2 > target:
                pointer_2 -= 1
                
            elif num1 + num2 < target:
                pointer_1 += 1
                
                
        return []
