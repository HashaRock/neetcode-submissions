class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for n, cnt in dict.items():
            freq[cnt].append(n)
        res = []
        for j in range(len(freq) - 1, 0, -1):
            for num in freq[j]:
                res.append(num)
                if len(res) == k:
                    return res