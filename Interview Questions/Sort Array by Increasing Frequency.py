class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = {}
        final_ans = []
        
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        
        ordered_dict = dict(sorted(result.items(), key=lambda item: (item[1], -item[0])))
        
        for k,v in ordered_dict.items():
            final_ans = final_ans + [k]*v
            
        return final_ans
