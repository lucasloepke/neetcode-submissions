class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        squares = [set() for x in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                sindex = (i // 3) * 3 + (j // 3)

                if val in rows[i] or val in cols[j] or val in squares[sindex]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[sindex].add(val)

        return True