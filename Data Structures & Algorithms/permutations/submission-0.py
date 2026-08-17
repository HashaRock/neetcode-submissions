class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        chosen = [False] * n

        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
            for i in range(n):
                if not chosen[i]:
                    chosen[i] = True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    chosen[i] = False
        
        dfs([])
        return res