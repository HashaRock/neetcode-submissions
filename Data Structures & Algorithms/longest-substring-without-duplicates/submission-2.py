class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        maxx = 0
        sset = set()
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            sset.add(s[r])
            maxx = max(maxx, r - l + 1)
        
        return maxx