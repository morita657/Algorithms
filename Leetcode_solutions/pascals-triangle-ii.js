/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
  const triangle = [];
  const numRows = rowIndex + 1;
  for (let i = 0; i < numRows; i++) {
    const row = [];
    for (let j = 0; j < i + 1; j++) {
      row.push(0);
    }
    row[0] = 1;
    row[row.length - 1] = 1;
    for (let k = 1; k < row.length - 1; k++) {
      row[k] = triangle[i - 1][k - 1] + triangle[i - 1][k];
    }
    triangle.push(row);
  }
  return triangle[rowIndex];
};
