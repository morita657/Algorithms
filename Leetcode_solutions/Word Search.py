class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    self.search(board, i, j, word)

    def search(self, board, i, j, word):
        if len(word) == 0:
            return
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]) or board[i][j] != word[0]:
            return
        else:
            if board[i][j] == word[0]:
                word = word[1:]
                self.search(board, i + 1, j, word)
                self.search(board, i - 1, j, word)
                self.search(board, i, j + 1, word)
                self.search(board, i, j - 1, word)
        return len(word) == 0


class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
            or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res
