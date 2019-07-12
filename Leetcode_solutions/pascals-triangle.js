/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  const first = [1],
    second = [1, 1],
    result = [first, second];
  if (numRows === 0) return [];
  else if (numRows === 1) return [[1]];
  else if (numRows === 2) return [[1], [1, 1]];
  else {
    numRows = numRows - 2;
    while (numRows !== 0) {
      elem = result[result.length - 1];
      newRow = [1];
      for (let i = 0; i < elem.length - 1; i++) {
        newElem = elem[i] + elem[i + 1];
        newRow.push(newElem);
      }
      newRow.push(1);
      result.push(newRow);
      numRows--;
    }
    return result;
  }
};

console.log(generate(5));
console.log(generate(0));
console.log(generate(1));
console.log(generate(2));
