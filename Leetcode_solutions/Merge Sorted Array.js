/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  nums1.splice(m, nums1.length);
  nums2.splice(n, nums2.length);
  let i = 0,
    j = 0;
  while (j < n) {
    if (nums2[j] < nums1[i] || nums1[i] === undefined) {
      nums1.splice(i, 0, nums2[j]);
      i++;
      j++;
    } else {
      i++;
    }
  }
};
