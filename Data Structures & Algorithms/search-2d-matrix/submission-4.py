class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n - 1)

        while l <= r:
            middle = l + (r - l) // 2
            i, j = middle // n, middle % n

            mid = matrix[i][j]

            if target == mid:
                return True
            elif target < mid:
                r = middle - 1
            else:
                l = middle + 1

        return False