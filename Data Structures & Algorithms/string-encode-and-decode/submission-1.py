class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        szs, res = [], ""
        for s in strs:
            szs.append(len(s))
        for sz in szs:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        szs, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            szs.append(int(cur))
            i += 1
        i += 1
        for sz in szs:
            res.append(s[i:i + sz])
            i += sz
        return res