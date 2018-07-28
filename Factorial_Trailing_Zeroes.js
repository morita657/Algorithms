/**
 * @param {number} n
 * @return {number}
 */
const trailingZeroes = function(n) {
  let sum = 0;
  while (n >= 5) {
    sum += Math.floor((n /= 5));
  }
  return sum;
};
