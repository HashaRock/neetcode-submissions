class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for chart in t:
            dict_t[chart] = dict_t.get(chart, 0) + 1
        return dict_s == dict_t