/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  memo = [];
  for (let i = 0; i < nums.length; i++) {
    if (memo.includes(nums[i])) return true;
    memo.push(nums[i]);
  }
  return false;
};
