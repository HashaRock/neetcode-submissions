class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result, prefix, suffix = [0] * n, [0] * n, [0] * n
        prefix[0] = suffix[-1] = 1
        for i in range (1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range (n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range (n):
            result[i] = prefix[i] * suffix[i]
        return result