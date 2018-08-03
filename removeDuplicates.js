/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = function(nums) {
  let i;
  for (i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i + 1]) {
      nums.splice(i, 1);
      i--;
    }
  }
  return i;
};
