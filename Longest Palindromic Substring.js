/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  if (s === null || s.length < 1) return "";
  // if (s.length === 1) return s;
  let start = 0,
    end = 0;
  for (let i = 0; i < s.length; i++) {
    let len1 = expandAroundCenter(s, i, i);
    let len2 = expandAroundCenter(s, i, i + 1);

    let len = Math.max(len1, len2);
    if (len > end - start) {
      start = i - (len - 1) / 2;
      end = i + len / 2;
    }
  }
  return s.substring(Math.ceil(start), end + 1);
};
const expandAroundCenter = (s, left, right) => {
  let l = left,
    r = right;
  while (l >= 0 && r < s.length && s.charAt(l) === s.charAt(r)) {
    l--;
    r++;
  }
  return r - l - 1;
};
