class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1, ind2 = 0, len(numbers) - 1
        while ind1 < ind2:
            cur = numbers[ind1] + numbers[ind2]
            if cur == target:
                return [ind1 + 1, ind2 + 1]
            elif cur < target:
                ind1 += 1
            else:
                ind2 -= 1
        return [-1]