/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const findKthLargest = function(nums, k) {
  //   sort array
  //     slice from back to find the kth value
  nums.sort((first, second) => second - first);
  console.log(nums);
  return nums[k - 1];
};
