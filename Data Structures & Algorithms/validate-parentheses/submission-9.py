class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque([])
        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        for ch in s:
            if ch in pairs:
                if stk and pairs[ch] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(ch)

        return not stk