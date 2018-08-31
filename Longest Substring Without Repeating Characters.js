/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  const n = s.length;
  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j <= n; j++) {
      if (allUnique(s, i, j)) ans = Math.max(ans, j - i);
    }
  }
  return ans;
};
const allUnique = (s, start, end) => {
  const set = new Set();
  for (let i = start; i < end; i++) {
    let ch = s.charAt(i);
    if (set.has(ch)) return false;
    set.add(ch);
  }
  return true;
};
