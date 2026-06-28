class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        keypad = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        makingcombo = []
        def backtrack(digitindex):
            if len(makingcombo) == len(digits):
                res.append("".join(makingcombo))
                return

            pad = keypad[int(digits[digitindex])]
            for ch in pad:
                makingcombo.append(ch)
                backtrack(digitindex + 1)
                makingcombo.pop()

        backtrack(0)
        return res
