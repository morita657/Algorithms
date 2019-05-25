/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  const str = x.toString();
  let front = "",
    back = "";
  for (let i = 0; i < str.length; i++) {
    front += str.slice(i, i + 1);
  }
  for (let j = str.length - 1; j >= 0; j--) {
    back += str.slice(j, j + 1);
  }
  return front === back;
};
