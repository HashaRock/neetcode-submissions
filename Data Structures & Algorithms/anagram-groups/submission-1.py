class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdct = defaultdict(list)

        for s in strs:
            keys = [0] * 26
            for ch in s:
                keys[ord('a') - ord(ch)] += 1
            strdct[tuple(keys)].append(s)
        
        return list(strdct.values())