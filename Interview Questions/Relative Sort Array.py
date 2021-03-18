class Solution:
    def relativeSortArray(self, arr1, arr2):
        dict={}
        nums,ans = [], []
        
        for val in arr2:
            dict[val] = 0
        
        for val in arr1:
            if val not in dict:
                nums.append(val)
            else: 
                dict[val] += 1
        
        for val, freq in dict.items():
            ans.extend([val for i in range(freq)])
        
        ans.extend(sorted(nums))
        return ans
        
