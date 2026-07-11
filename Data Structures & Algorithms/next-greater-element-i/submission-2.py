class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valtoidx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stk = deque([])
        for i in range(len(nums2)):
            cur = nums2[i]
            while stk and cur > stk[-1]:
                val = stk.pop()
                idx = valtoidx[val]
                res[idx] = cur
            if cur in valtoidx:
                stk.append(cur)
        return res