class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def bsch(left, right):
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1

        res = bsch(0, pivot - 1)
        if res != -1:
            return res
        return bsch(pivot, len(nums) - 1)