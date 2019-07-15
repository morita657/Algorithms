/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  curr = [];
  for (let i = 0; i < nums.length; i++) {
    if (curr.indexOf(nums[i]) >= 0) {
      curr.splice(curr.indexOf(nums[i]), 1);
    } else {
      curr.push(nums[i]);
    }
  }
  return curr[0];
};
console.log(singleNumber([2, 2, 1]));
