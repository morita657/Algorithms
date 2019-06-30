/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  const output = [];
  let total = 1;
  let current = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    output[i] = total;
    total *= nums[i];
  }
  for (let j = 0; j < nums.length; j++) {
    output[j] *= current;
    current *= nums[j];
  }
  return output;
};
