/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  (maxCur = 0), (maxSoFar = 0);
  for (let i = 1; i < prices.length; i++) {
    maxCur = Math.max(0, (maxCur += prices[i] - prices[i - 1]));
    maxSoFar = Math.max(maxCur, maxSoFar);
  }
  return maxSoFar;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
console.log(maxProfit([2, 4, 1]));
