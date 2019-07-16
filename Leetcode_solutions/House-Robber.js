/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let a = 0,
    b = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i % 2 == 0) {
      a = Math.max(a + nums[i], b);
    } else {
      b = Math.max(a, b + nums[i]);
    }
  }

  return Math.max(a, b);
};

console.log(rob([2, 1, 1, 2]));
console.log(rob([1, 2, 1, 1, 3]));
