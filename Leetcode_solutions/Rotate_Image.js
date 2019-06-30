/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const rotate = function(matrix) {
  matrix.reverse();
  const len = matrix.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      matrix[i].push(matrix[j][i]);
    }
  }
  for (let k = 0; k < len; k++) {
    matrix[k].splice(0, len);
  }
};
