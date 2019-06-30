/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
  let front = 0,
    back = nums.length;
  while (front < back) {
    if (nums[front] === val) {
      nums[front] = nums[back - 1];
      back--;
    } else {
      front++;
    }
  }
  return back;
};
