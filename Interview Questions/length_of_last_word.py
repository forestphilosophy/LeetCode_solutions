class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        str_l = s.split()
        
        last_word = str_l[-1]
        
        return len(last_word)
