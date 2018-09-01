/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  if (s.length === 1) return s;
  const result = [];
  for (let i = 0; i < s.length; i++) {
    for (let j = i; j <= s.length; j++) {
      if (isValid(s, i, j)) result.push(s.slice(i, j));
    }
  }
  result.sort();
  let longestWord = "";
  result.forEach((word) => {
    if (word.length > longestWord.length) longestWord = word;
  });
  return longestWord;
};
const isValid = (string, start, end) => {
  const reverse = string
    .slice(start, end)
    .split("")
    .reverse()
    .join("");
  return string.slice(start, end) === reverse;
};
