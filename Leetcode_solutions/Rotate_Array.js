/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const rotate = function(nums, k) {
  for (let i = 0; i < k; i++) {
    const num = nums.slice(-1)[0];
    nums.splice(-1, 1);
    nums.unshift(num);
  }
};
