class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = defaultdict(int)
        res = 0

        for r, fruit in enumerate(fruits):
            count[fruit] += 1

            while len(count) > 2:
                left_fruit = fruits[l]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                l += 1

            res = max(res, r - l + 1)

        return res