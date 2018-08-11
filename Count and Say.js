/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
  let current = "1";
  for (let i = 1; i < n; i++) {
    current = counter(current);
  }
  return current;
};

const counter = (input) => {
  let count = 1,
    output = "";
  const memo = [];
  for (let i = 1; i <= input.length; i++) {
    if (input[i] === input[i - 1]) {
      count++;
    }
    if (input[i] !== input[i - 1]) {
      memo.push(`${count}${input[i - 1]}`);
      count = 1;
    }
  }
  for (let j = 0; j < memo.length; j++) {
    output += memo[j];
  }
  return output;
};
