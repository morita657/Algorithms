/**
 * @param {number} n
 * @return {boolean}
 */
const isPowerOfThree = function(n) {
  const results = [];
  let i = 0;
  while (i < 30) {
    results.push(Math.pow(3, i));
    i++;
  }
  return results.includes(n);
};
