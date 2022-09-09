class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join([str(digit) for digit in digits])
        
        num = int(num_str)
        
        ans = num + 1
        
        num_str = [str for str in str(ans)]
        
        result = [int(str) for str in num_str]
        
        return result
