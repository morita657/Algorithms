var square = 6;
var count = 0;
var is_used = new Array();
for (var i = 0; i <= square; i++) {
  is_used[i] = new Array();
  for (var j = 0; j <= square; j++) {
    is_used[i][j] = new Array(false, false);
  }
}
console.log("is_used: ", is_used);

// console.log("is_used: ", is_used);
// 行きと帰りで違うパターンの通れる数を求める
// if n=1
//  -
// | |
//  -
// if n=2
//  --
// | |
// | |
//  --
// if n=3
// ---
// |  |
// |  |
// |  |
// ---
// if n=4
// ----
// |   |
// |   |
// |   |
// |   |
// ----
function route(x, y, is_first_time) {
  // if reached to the goal and if this is not the first time, count as 1
  if (x == square && y == square) {
    // console.log(x, y);
    if (is_first_time) {
      route(0, 0, false);
    } else {
      count++;
    }
  }
  //   if movable to x-coordination
  if (x < square) {
    if (!is_used[x][y][0]) {
      console.log("is_used[x][y][0]: ", is_used[x][y][0]);

      is_used[x][y][0] = true;
      route(x + 1, y, is_first_time);
      is_used[x][y][0] = false;
    }
  }
  //   if movable to y-coordination
  if (y < square) {
    if (!is_used[x][y][1]) {
      is_used[x][y][1] = true;
      route(x, y + 1, is_first_time);
      is_used[x][y][1] = false;
    }
  }
  console.log("is_used: ", is_used);
}
route(0, 0, true);
console.log(count);
