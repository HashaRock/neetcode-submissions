class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sset = set(nums)
        maxx = 0
        for n in nums:
            if n - 1 not in sset:
                conseq = 1
                x = n + 1
                while x in sset:
                    x += 1
                    conseq += 1
                maxx = max(maxx, conseq)
        return maxx
                