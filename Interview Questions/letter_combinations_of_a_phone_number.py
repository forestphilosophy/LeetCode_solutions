from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {'2':'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}
        
        len_digits = len(digits)
        
        if len_digits == 0:
            return []
        
        list_of_letters = []
        for digit in digits:
            list_of_letters.append(mapping[digit])
        
        return list(map("".join, itertools.product(*list_of_letters)))
