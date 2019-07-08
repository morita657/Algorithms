/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
  const candidates = [];
  let candidate = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        candidate = nums[i] + nums[j] + nums[k];
        candidates.push(candidate);
      }
    }
  }
  let curr = candidates[0];
  for (let l = 0; l < candidates.length; l++) {
    if (Math.abs(target - candidates[l]) < Math.abs(target - curr)) {
      curr = candidates[l];
    }
  }
  return curr;
};
