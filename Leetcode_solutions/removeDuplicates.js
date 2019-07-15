/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = function(nums) {
  index = 0;
  copy = nums;
  while (index < copy.length) {
    if (copy[index] === copy[index + 1]) {
      nums.splice(index, 1);
    }
    index++;
  }
  copy = nums;
  while (index >= 0) {
    if (copy[index] === copy[index - 1]) {
      nums.splice(index, 1);
    }
    index--;
  }
  return nums.length;
};
