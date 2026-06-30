class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        def sortkey(n):
            return (counts[n], -n)

        nums.sort(key=sortkey)

        return nums