board = [[1, 2], [2, 3], [7, 8], [8, 9], [1, 4], [3, 6], [4, 7], [6, 9]];
for (let i = 1; i <= 9; i++) {
  board.push([i]);
}

function strike(_board) {
  cnt = 0;
  for (let i = 0; i < _board.length; i++) {
    next_board = select(_board, _board[i]);
    cnt += strike(next_board);
  }

  return cnt;
}

function select(brd, b) {
  for (let i = 0; i < brd.length; i++) {
    if ((brd[i] && b) === 0) {
      return;
    }
  }
}

console.log(strike(board));
