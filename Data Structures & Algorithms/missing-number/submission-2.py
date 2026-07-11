from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numsSum = reduce(lambda x, y: x + y, nums)
        rangeSum = reduce(lambda x, y: x + y, range(len(nums) + 1))

        return rangeSum - numsSum