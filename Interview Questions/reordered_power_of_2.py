import itertools
import numpy as np
class Solution:
    
    def _get_freq_dict(self,n):
        freq = dict()
        
        for num in str(n):
            if num not in freq:
                freq[num] = 0
                
            else:
                freq[num] += 1
        
        return freq
    
    def reorderedPowerOf2(self, n: int) -> bool:
        
        freq_n = self._get_freq_dict(n)
        num_of_digits = len(str(n))
        for i in range(30):
            
            num = 2**i
            
            if self._get_freq_dict(num) == freq_n and len(str(num)) == num_of_digits:
                return True
        
        return False
            
            
            
