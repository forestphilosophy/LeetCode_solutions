class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        ans = 0
        unique = set(s)
        table = {k:0 for k in unique}
        for i in range(len(s)):         
            tmp = 0
            
            for j in range(i,len(s)):
                if table[s[j]] == 0: # not occured
                    table[s[j]] = 1
                    tmp += 1

                else: #already occured
                    table = {k:0 for k in unique} # reset the table
                    break

            ans = max(tmp,ans)

        return ans
