/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  return climb(0, n);
};
const climb = (i, target) => {
  if (i > target) return 0;
  if (i === target) return 1;
  return climb(i + 1, target) + climb(i + 2, target);
};
