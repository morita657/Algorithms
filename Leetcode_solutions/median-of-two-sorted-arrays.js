/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  //   merge two arrays
  //     sort the merged array
  const mergedArr = nums1.concat(nums2).sort((a, b) => a - b);
  const len = mergedArr.length;
  //     if the number of elements is odd, find middle
  if (len % 2 !== 0) {
    return mergedArr[Math.round(len / 2) - 1];
  }
  //     else find two elements in the middle, then plus them and divide by 2
  else {
    const first = Math.round(len / 2),
      second = Math.round(len / 2 - 1),
      median = (mergedArr[first] + mergedArr[second]) / 2;
    return median;
  }
};
