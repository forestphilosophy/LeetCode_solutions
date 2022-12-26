from itertools import permutations
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sorted_s1 = ''.join(sorted(s1))

        length = len(s1)

        substrings = []

        first = 0
        last = first + length

        while last <= len(s2):
            substrings += [''.join(sorted(s2[first:last]))]
            first += 1
            last += 1
            
        if sorted_s1 in substrings:
            return True

        else:
            return False

            
