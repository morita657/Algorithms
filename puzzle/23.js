/**
 *
 * @param {*} coin
 * @param {*} depth the number of game
 */
function game(coin, depth) {
  if (coin === 0) {
    return 0;
  }
  if (depth === 1) {
    return 1;
  }
  win = game(coin + 1, depth - 1);
  lose = game(coin - 1, depth - 1);

  return win + lose;
}

console.log(game(10, 24));
