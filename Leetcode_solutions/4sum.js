/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
  const candidates = {};
  let m = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        for (let l = k + 1; l < nums.length; l++) {
          candidate = nums[i] + nums[j] + nums[k] + nums[l];
          candidates[m] = [nums[i], nums[j], nums[k], nums[l]];
          m++;
        }
      }
    }
  }
  const solutions = [];
  const targets = Object.keys(candidates);
  for (let i = 0; i < targets.length; i++) {
    const reducer = (accumulator, currentValue) => accumulator + currentValue;
    let sum = candidates[i].reduce(reducer, 0);
    if (sum === target) {
      solutions.push(candidates[i]);
    }
  }
  return solutions;
};
