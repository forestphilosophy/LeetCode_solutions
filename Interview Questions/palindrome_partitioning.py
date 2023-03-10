class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        
        @cache
        def dfs(s):
            if not s: return [[]]
            
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                    for suf in self.partition(s[i:]):  # process suffix recursively
                        ans.append([s[:i]] + suf)
            return ans

        return dfs(s)
