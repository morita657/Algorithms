/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
  let len = 0,
    l = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== " ") {
      l = len++;
    } else if (s == " ") {
      len = 0;
    }
  }
  return l;
};
console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord(""));
console.log(lengthOfLastWord("a "));
console.log(lengthOfLastWord("a"));
console.log(lengthOfLastWord("Today is a nice day"));
