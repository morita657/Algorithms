/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  zeros = [];
  for (let i = 0; i < nums.length; i++) {
    if (copy[i] === 0) {
      zeros.push(copy[i]);
      nums.splice(i, 1);
      i--;
    }
  }
  for (let i = 0; i < zeros.length; i++) {
    nums.push(zeros[i]);
  }

  return nums;
};
console.log(moveZeroes([0, 1, 0, 3, 12]));
console.log(moveZeroes([0, 0, 1]));
console.log(moveZeroes([0, 0, 0, 1]));
console.log(moveZeroes([0, 1, 0, 3, 0, 0, 0, 12]));
