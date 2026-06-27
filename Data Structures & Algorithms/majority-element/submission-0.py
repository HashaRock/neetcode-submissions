class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        maxk, maxoc = 0, 0
        for key, value in count.items():
            if maxoc < value:
                maxk = key
                maxoc = value
            
        return maxk