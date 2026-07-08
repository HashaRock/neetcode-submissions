class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        wset = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in wset:
                wset.remove(s[l])
                l += 1
            wset.add(s[r])
            res = max(res, r - l + 1)
        
        return res