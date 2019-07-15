/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  combination = [];
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        combination.push(i, j);
      }
    }
  }
  return combination;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  store = {};
  for (let i = 0; i < nums.length; i++) {
    m = target - nums[i];
    if (m in store) {
      return [i, store[m]];
    } else {
      store[nums[i]] = i;
    }
  }
  return null;
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
