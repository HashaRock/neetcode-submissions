class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        sub = []
        def backtrack(i):
            if i == len(nums):
                sol.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i + 1)
            sub.pop()
            backtrack(i + 1)

        backtrack(0)
        return sol