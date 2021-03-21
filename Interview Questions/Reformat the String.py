class Solution:
    def reformat(self, s: str) -> str:
        letters = [let for let in s if let.isalpha()]
        nums = [num for num in s if not num.isalpha()]
        
        if len(s) == 1:
            return ''.join(s)
        if (not letters) or (not nums):
            return ""
        
        idx = 1
        if len(nums) >= len(letters):
            for i in range(len(nums)):
                try:
                    nums.insert(i+idx,letters[i])
                    idx += 1
                except:
                    continue

            return (''.join(nums))
        else:
            for i in range(len(letters)):
                try:
                    letters.insert(i+idx,nums[i])
                    idx += 1
                except:
                    continue
            return (''.join(letters))
