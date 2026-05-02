class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxd, l, r = 0, 0, len(heights) - 1
        
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxd = max(maxd, area)
        
        return maxd