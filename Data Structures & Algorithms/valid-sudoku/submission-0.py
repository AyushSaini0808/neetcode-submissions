class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS=defaultdict(set)
        COLS=defaultdict(set)
        squares=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in ROWS[i]) or (board[i][j] in COLS[j]) or (board[i][j] in squares[(i//3,j//3)]):
                    return False
                ROWS[i].add(board[i][j])
                COLS[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True