class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_list = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                sum_list.append(sum(nums[i:j]))
                
        sum_list = sorted(sum_list)
        ans = sum(sum_list[left-1:right])
        
        return ans%(10**9 + 7)
