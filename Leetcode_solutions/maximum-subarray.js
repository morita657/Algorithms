/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  max_sum = Number.NEGATIVE_INFINITY;
  let i = 0,
    j = 0;
  while (i < nums.length) {
    let sum = 0;
    while (j < nums.length) {
      sum += nums[j];
      if (sum > max_sum) {
        max_sum = sum;
      }
      if (nums[j] > sum) {
        break;
      } else {
        j++;
      }
    }
    i = j;
  }
  return max_sum;
};
console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));

console.log(maxSubArray([-1]));
