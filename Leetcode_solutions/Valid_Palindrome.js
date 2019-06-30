/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function(s) {
  const str = s.replace(/[^A-Za-z0-9_]/gi, "").toLowerCase();
  const reverse = str
    .split("")
    .reverse()
    .join("");
  return str === reverse;
};
