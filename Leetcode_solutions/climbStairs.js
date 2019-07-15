/**
 * @param {number} n steps of the stair
 * @return {number}
 */
// var climbStairs = function(n) {
//   cache = {};
//   (cache[1] = 1), (cache[2] = 2);

//   for (let i = 3; i < n + 1; i++) {
//     cache[i] = cache[i - 1] + cache[i - 2];
//   }
//   return cache[n];
// };

function climbStairs(n) {
  let q = [[1, 1], [1, 0]];
  let res = pow(q, n);
  return res[0][0];
}
function pow(a, n) {
  let ret = [[1, 0], [0, 1]];
  while (n > 0) {
    if ((n & 1) == 1) {
      ret = multiply(ret, a);
    }
    n >>= 1;
    a = multiply(a, a);
  }
  return ret;
}

function multiply(a, b) {
  c = [[], []];
  for (let i = 0; i < 2; i++) {
    for (let j = 0; j < 2; j++) {
      c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
    }
  }
  return c;
}

function climbStairs(n) {
  sqrt5 = Math.sqrt(5);
  fibn = Math.pow((1 + sqrt5) / 2, n + 1) - Math.pow((1 - sqrt5) / 2, n + 1);
  return fibn / sqrt5;
}
console.log(climbStairs(2));
console.log(climbStairs(3));
console.log(climbStairs(4));
