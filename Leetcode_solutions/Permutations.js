/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permute = function(nums) {
  const result = [];
  const makePermutation = (input, position) => {
    // base case
    if (input.length - 1 === position) {
      result.push(input);
      return result;
    }
    // recursive case
    else {
      for (let i = position; i < input.length; i++) {
        temp = input[position];
        input.splice(position, 1, input[i]);
        input.splice(i, 1, temp);
        makePermutation(input.slice(), position + 1);
      }
    }
  };
  makePermutation(nums, 0);
  return result;
};
