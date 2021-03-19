class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_list = [i for i in nums if i % 2 == 0]
        odd_list = [i for i in nums if i % 2 != 0]
        
        idx = 1
        for i in range(len(even_list)):
            even_list.insert(idx,odd_list[i])
            idx += 2
        
        return even_list
