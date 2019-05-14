/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
  let i = 0;
  while (i < nums.length) {
    if (nums[i] === val && i !== 0) {
      nums = nums.slice(0, i).concat(nums.slice(i + 1));
    } else if (nums[i] === val && i == 0) {
      nums = nums.slice(1);
    }
    i++;
  }
  while (i > 0) {
    if (nums[i] === val && i !== nums.length - 1) {
      nums = nums.slice(0, i).concat(nums.slice(i + 1));
    } else if (nums[i] === val && i == nums.length) {
      nums = nums.slice(0, i - 1);
    }
    i--;
  }

  return nums;
};
