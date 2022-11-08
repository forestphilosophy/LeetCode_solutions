class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums = sorted(nums)

        for idx,num in enumerate(nums):

            two_sum_target = 0 - num
            
            left_pointer = idx + 1
            right_pointer = len(nums) - 1
            
            while left_pointer < right_pointer:
                
                two_sum = nums[left_pointer] + nums[right_pointer] 
                
                if two_sum > two_sum_target:
                    right_pointer -= 1
                
                elif two_sum < two_sum_target:
                    left_pointer += 1
                
                elif two_sum == two_sum_target:
                    _res = sorted([num,nums[left_pointer],nums[right_pointer]])
                    if _res not in res:
                        res.append(_res)
                    right_pointer -= 1
                    left_pointer += 1
                    
        return res
