class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sset = set(nums)

        for i in range(len(nums)):
            if i not in sset:
                return i
        
        return len(nums)