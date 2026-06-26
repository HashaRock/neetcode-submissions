class Solution:
    def isPalindrome(self, s: str) -> bool:
        cuh = []
        for ch in s:
            if self.alphaNum(ch):
                cuh.append(ch)
        sAlpha = cuh
        l, r = 0, len(sAlpha) - 1
        while l < r:
            if sAlpha[l].lower() != sAlpha[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))