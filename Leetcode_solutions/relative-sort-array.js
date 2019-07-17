/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
  res = [];
  copy = arr1;
  let i = 0;
  while (i < arr2.length) {
    for (let j = 0; j < copy.length; j++) {
      if (copy[j] === arr2[i]) {
        res.push(copy[j]);
        arr1.splice(j, 1);
        j--;
      }
    }
    i++;
  }
  arr1 = arr1.sort((a, b) => a - b);
  return res.concat(arr1);
};
console.log(
  relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
);
