class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        bin_str_start = "{0:b}".format(start)
        bin_str_goal = "{0:b}".format(goal)
        
        if len(bin_str_start) > len(bin_str_goal):
            bin_str_goal = bin_str_goal.zfill(len(bin_str_start))
        
        elif len(bin_str_start) < len(bin_str_goal):
            bin_str_start = bin_str_start.zfill(len(bin_str_goal))
        
        res = sum(1 for a, b in zip(bin_str_start, bin_str_goal) if a != b)
        
        return res
