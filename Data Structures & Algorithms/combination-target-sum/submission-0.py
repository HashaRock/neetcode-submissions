class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, currsum):
            if currsum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or currsum > target:
                return

            curr.append(nums[i])
            backtrack(i, curr, currsum + nums[i])
            curr.pop()
            backtrack(i + 1, curr, currsum)
            

        backtrack(0, [], 0)
        return res