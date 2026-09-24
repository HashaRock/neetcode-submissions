class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        twoback = 1
        oneback = 2

        for i in range(2, n):
            curr = twoback + oneback
            twoback = oneback
            oneback = curr
        
        return curr