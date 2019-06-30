/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function(nums) {
  const candidates = {};
  for (let i = 0; i < nums.length; i++) {
    if (candidates.hasOwnProperty(nums[i])) {
      candidates[nums[i]] += 1;
    } else {
      candidates[nums[i]] = 1;
    }
  }
  for (let key in candidates) {
    if (candidates[key] > 1) {
      return true;
    }
  }
  return false;
};
