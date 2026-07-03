class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            squ = m * m
            if squ < x:
                l = m + 1
                res = m
            elif squ > x:
                r = m - 1
            else:
                return m
        
        return res