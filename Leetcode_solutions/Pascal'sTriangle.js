/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows, row = 0, column = 1, output = [[1]]) {
  // i row
  // j column
  // base
  if (numRows === 0) {
    return [];
  }
  if (row > numRows) {
    return output;
  } else {
    if (row >= output.length) {
      output.push([]);
      output[row].push(1);
      for (let i = 1; i < row; i++) {
        output[row].push(output[row - 1][i - 1] + output[row - 1][i]);
      }
      output[row].push(1);
    }
    return generate(numRows, row + 1, column++, output);
  }
};
console.log(generate(3));
console.log(generate(5));
