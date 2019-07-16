/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  (soFar = nums[0]), (maxSum = nums[0]);
  for (let i = 1; i < nums.length; i++) {
    soFar = Math.max(nums[i], (soFar += nums[i]));
    maxSum = Math.max(soFar, maxSum);
  }
  return maxSum;
};
