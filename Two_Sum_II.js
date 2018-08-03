/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
  const len = numbers.length;
  let i = 0,
    j = len - 1;
  while (numbers[i] + numbers[j] !== target) {
    numbers[i] + numbers[j] > target ? j-- : i++;
  }
  return [i + 1, j + 1];
};
