class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][1]:
                result[stk[-1][0]] = i - stk[-1][0]
                stk.pop()
            stk.append((i, temp))
        
        return result