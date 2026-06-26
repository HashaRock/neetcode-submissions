from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = [0]
        n = len(nums)
        subset = []

        def backtrack(i):
            if subset:
                sum[0] += reduce(xor, subset)

            for x in range(i, n):
                subset.append(nums[x])
                backtrack(x + 1)
                subset.remove(nums[x])
        
        backtrack(0)
        return sum[0]