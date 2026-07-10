class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        stk = deque([])

        for ch in s:
            if ch in pairs:
                if not stk or pairs[ch] != stk.pop():
                    return False
            else:
                stk.append(ch)

        return not stk