class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_min = 0
        left_max = 0
        
        for letter in s:
            
            if letter == '(':
                left_min += 1
                left_max += 1
            
            elif letter == ')':
                left_min -= 1
                left_max -= 1
                
            elif letter == '*':
                left_min -= 1
                left_max += 1                
                
            if left_max < 0:
                return False
            
            if left_min < 0:
                left_min = 0
            
        if left_min <= 0 <= left_max:
            return True
            
