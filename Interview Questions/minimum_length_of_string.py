class Solution:
    def minimumLength(self, s: str) -> int:

        left = 0
        right = len(s) - 1
        letter_removed = ''
        while left <= right:
            #print(s[left:right+1])
            if left == right:
                if s[left] == letter_removed:
                    return 0
                else:
                    return 1

            if s[left] == s[right]:
                if s[left+1] == s[right]:
                    letter_removed = s[right]
                    left += 1
                    continue

                elif s[right-1] == s[left]:
                    letter_removed = s[left]
                    right -= 1
                    continue
                
                else:
                    left += 1
                    right -= 1
                    continue

            else:
                return len(s[left:right+1])

        return 0
