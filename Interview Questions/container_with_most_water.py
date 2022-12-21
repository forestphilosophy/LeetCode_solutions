class Solution:
    def maxArea(self, height: List[int]) -> int:

        first = 0
        last = len(height) - 1
        max_area = min(height[first],height[last]) * (last - first)

        while first < last:

            max_area = max(max_area,(min(height[first],height[last]) * (last - first)))
            if height[first] > height[last]:
                last -= 1

            elif height[first] <= height[last]:
                first += 1


        return max_area 
