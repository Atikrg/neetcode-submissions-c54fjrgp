class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left  = 0

        right = len(heights) - 1
        max_water = 0

        for i in range(len(heights)):
            area = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, area)

            if heights[left] < heights[right]:
                left+=1

            else:
                right -= 1

        return max_water