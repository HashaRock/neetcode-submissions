import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        maxPile = max(piles)
        l, r = 1, maxPile
        mink = maxPile

        while l <= r:
            k = l + (r - l) // 2
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile / k)

            if hoursTaken <= h:
                mink = min(mink, k)
                r = k - 1
            else:
                l = k + 1
        
        return mink