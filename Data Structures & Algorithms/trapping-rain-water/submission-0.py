class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suff = [0] * len(height)
        maxWater = 0

        for i in range(1, len(height)):
            pref[i] = max(pref[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i + 1])
        
        for ind in range(len(height)):
            maxWater += max(0, min(pref[ind], suff[ind]) - height[ind])
        
        return maxWater
        
