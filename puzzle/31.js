var square = 3;
var count = 0;
var is_used = new Array();
for (var i = 0; i <= square; i++) {
  is_used[i] = new Array();
  for (var j = 0; j <= square; j++) {
    is_used[i][j] = new Array(false, false);
  }
}
// console.log("is_used: ", is_used);

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
    if (is_first_time) {
      route(0, 0, false);
    } else {
      count++;
    }
  }
  //   if movable to x-coordination
  if (x < square) {
    if (!is_used[x][y][0]) {
      is_used[x][y][0] = true;
      //   console.log("before: ", is_used);
      route(x + 1, y, is_first_time);
      is_used[x][y][0] = false;
      //   console.log("after: ", is_used);
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
}
// route(0, 0, true);
// console.log(count);

// Different pattern
function route(width, height, back_y) {
  if (width == 1) {
    return back_y == height ? back_y : back_y + 2;
  }
  if (height == 1) {
    return back_y == 0 ? 2 : 1;
  }
  var total = 0;
  if (back_y == 0) {
    for (var i = 0; i < height; i++) {
      total += 2 * route(width - 1, height, i + 1);
    }
  } else {
    for (var i = back_y; i <= height; i++) {
      total += route(width - 1, height, i);
    }
    total += route(width, height - 1, back_y - 1);
  }
  return total;
}

console.log(route(3, 3, 0));
