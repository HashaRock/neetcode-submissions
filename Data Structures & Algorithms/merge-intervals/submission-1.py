class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        res = [intervals[0]]
        for st, end in intervals:
            lastEnd = res[-1][1]

            if st <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([st, end])
        
        return res