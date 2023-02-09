class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        x_y = 0
        y_x = 0

        for str1,str2 in zip(s1,s2):

            if str1 == 'x' and str2 == 'y':
                x_y += 1

            if str1 == 'y' and str2 == 'x':
                y_x += 1
        
        if (x_y + y_x) % 2 != 0:
            return -1

        swaps = 0

        swaps += (x_y // 2)
        swaps += (y_x // 2)

        if x_y % 2 != 0:
            swaps += 2

        return swaps
