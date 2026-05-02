class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxd = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            maxd = max(count, maxd)
        
        return maxd