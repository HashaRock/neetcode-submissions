class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows, cols, sq = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range (9):
                val = board[r][c]
                if val != '.':
                    if (val in rows[r] or val in cols[c] or 
                        val in sq[(r // 3, c // 3)]):
                        return False
                    cols[c].add(val)
                    rows[r].add(val)
                    sq[(r // 3, c // 3)].add(val)

        return True
