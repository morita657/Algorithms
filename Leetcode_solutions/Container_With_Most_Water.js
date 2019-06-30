/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  let left = 0,
    right = height.length - 1,
    area = 0;
  while (left < right) {
    let currentArea = (right - left) * Math.min(height[left], height[right]);
    if (area < currentArea) {
      area = currentArea;
    }
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return area;
};
