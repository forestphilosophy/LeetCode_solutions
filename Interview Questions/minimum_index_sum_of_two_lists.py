class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words = dict()
        common_words = list(set(list(set(list1).intersection(list2))))
        
        for word in common_words:
            i = list1.index(word)
            j = list2.index(word)
            idx_sum = i + j
            
            words[word] = idx_sum
        
        min_idx = min(words.values())
        res = [k for k, v in words.items() if v==min_idx]
        
        return res
        
        
        
            
        
            
            
