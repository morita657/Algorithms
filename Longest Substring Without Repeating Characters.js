/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  const n = s.length;
  let ans = 0;
  const map = new Map();
  for (let j = 0, i = 0; j < n; j++) {
    if (map.has(s.charAt(j))) {
      i = Math.max(map.get(s.charAt(j)), i);
    }
    ans = Math.max(ans, j - i + 1);
    map.set(s.charAt(j), j + 1);
  }
  return ans;
};
