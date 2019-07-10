/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
  const spS = s.split(" ");
  const len = spS.length;
  for (let i = len - 1; i >= 0; i--) {
    if (spS[i] !== "") {
      return spS[i].length;
    }
  }
};
