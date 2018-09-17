function makeLists(n) {
  const result = [];
  for (let i = 0; i < n; i++) {
    result.push([]);
  }
  return result;
}

// console.log(makeLists(3));
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows === 1) return s;
  const result = makeLists(numRows);
  let curRow = 0,
    goingDown = false;
  for (let i = 0; i < s.length; i++) {
    result[curRow].push(s[i]);
    if (curRow === 0) {
      goingDown = true;
    } else if (curRow === numRows - 1) {
      goingDown = false;
    }
    if (goingDown) {
      curRow += 1;
    } else {
      curRow -= 1;
    }
  }
  let convertedStr = "";
  result.forEach((row) => {
    return row.forEach((chr) => {
      convertedStr += chr;
      return convertedStr;
    });
  });
  return convertedStr;
};
