class Solution:
    
    def get_product(self,nums: List[int])-> int:
        product = 1
        for i in nums:
            product *= i
        return product    
    
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums = sorted(nums,reverse = True)
        #Logic -> result has to be either the product of three largest numbers or the two smallest numbers multiplied by the largest number
        l1 = nums[0:3]
        l2 = nums[-2:] + [max(nums)]

        return max(self.get_product(l1),self.get_product(l2))
