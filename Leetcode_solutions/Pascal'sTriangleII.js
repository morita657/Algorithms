/**
 * @param {number} rowIndex
 * @return {number[]}
 */

var getRow = function(rowIndex, row = 0, column = 1, output = [[1]]) {
  // i row
  // j column
  // base
  if (rowIndex === 0) {
    return [1];
  }
  if (row > rowIndex) {
    return output[rowIndex];
  } else {
    if (row >= output.length) {
      output.push([]);
      output[row].push(1);
      if (row > 1) {
        for (let i = 1; i < row; i++) {
          output[row].push(output[row - 1][i - 1] + output[row - 1][i]);
        }
      }
      output[row].push(1);
    }
    return getRow(rowIndex, row + 1, column++, output);
  }
};

console.log(getRow(3));
