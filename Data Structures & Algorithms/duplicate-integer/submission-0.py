class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict and dict[i] >= 1:
                return True
            dict[i] = dict.get(i, 0) + 1
        return False