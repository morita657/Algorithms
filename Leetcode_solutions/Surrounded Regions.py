class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board) - 1:
                    if board[i - 1][j] == "X" and board[i + 1][j] == "X" and board[i][j - 1] == "X" and board[i][j + 1] == "X" and board[i][j] == "O":
                        board[i][j] = "S"
                else:
                    if board[i][j] == "O":
                        board[i][j] = "S"
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "S":
                    board[i][j] = "X"
        return board
