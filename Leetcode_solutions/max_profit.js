function main(prices) {
  let minv = prices[0],
    maxv = -Infinity;
  for (let j = 1; j < prices.length; j++) {
    if (maxv > prices[j] - minv) {
      maxv = maxv;
    } else {
      maxv = prices[j] - minv;
    }
    if (minv < prices[j]) {
      minv = minv;
    } else {
      minv = prices[j];
    }
  }

  return maxv - minv;
}
console.log(main([6, 5, 3, 1, 3, 4, 3]));
console.log(main([3, 4, 3, 2]));
