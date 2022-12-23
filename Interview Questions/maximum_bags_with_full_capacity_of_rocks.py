import numpy as np
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rocks_to_fill = list(np.subtract(capacity,rocks))
        n = len(capacity)
        bags = list(range(n))
        _dict = dict(zip(bags, map(list, zip(*(map(int, lst) for lst in (capacity, rocks, rocks_to_fill))))))
        
        _dict = sorted(_dict.items(), key=lambda x: x[1][2])
        print(_dict)
        final_ans = 0

        for item in _dict:

            if additionalRocks == 0:
                return final_ans

            rocks_to_fill = item[1][2]
            if rocks_to_fill == 0:
                final_ans += 1
                continue
            
            else:
                if rocks_to_fill <= additionalRocks:
                    additionalRocks -= rocks_to_fill
                    final_ans += 1
                else:
                    return final_ans

        return final_ans
