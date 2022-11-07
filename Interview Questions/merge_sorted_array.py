class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        _nums1 = nums1[:m]
        
        nums_combined = _nums1 + nums2
        
        nums_combined = sorted(nums_combined)
        
        for i in range(len(nums1)):
            nums1[i] = nums_combined[i]
