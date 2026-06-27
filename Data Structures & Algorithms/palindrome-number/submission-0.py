class Solution:
    def isPalindrome(self, x: int) -> bool:
        xst = str(x)

        l, r = 0, len(xst) - 1

        while l < r:
            if xst[l] != xst[r]:
                return False
            l += 1
            r -= 1

        return True