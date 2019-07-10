/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  //     make new empty array, push each element to the array
  //     if find the last element and plus one
  const res = [];
  for (let i = 0; i < digits.length; i++) {
    if (i === digits.length - 1) {
      res.push(digits[i] + 1);
    } else {
      res.push(digits[i]);
    }
  }
  return res;
};
