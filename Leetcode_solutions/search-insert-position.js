/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  //   loop in, if there is target in nums, return the index
  // else
  //     find the bigger value than target
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      return i;
    }
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > target) {
      return i;
    } else if (i === nums.length - 1) {
      return i + 1;
    }
  }
};
