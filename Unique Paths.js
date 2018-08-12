function makeBoard(row, col) {
  board = [];
  for (let i = 0; i < row; i++) {
    board.push([]);
    for (let j = 0; j < col; j++) {
      board[i].push(1);
    }
  }
  return board;
}

const uniquePaths = function(m, n) {
  const matrix = new makeBoard(m, n);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
    }
  }
  return matrix[m - 1][n - 1];
};
