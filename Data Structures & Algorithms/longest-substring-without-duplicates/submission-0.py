class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        workingSet = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in workingSet:
                workingSet.remove(s[l])
                l += 1
            workingSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen