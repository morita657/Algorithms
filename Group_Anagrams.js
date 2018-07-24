/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = function(strs) {
  const set = {};
  let result = [];
  for (let i = 0; i < strs.length; i++) {
    let a = strs[i].split("").sort();
    if (set.hasOwnProperty(`${a}`)) {
      set[`${a}`].push(strs[i]);
    } else {
      set[`${a}`] = [strs[i]];
    }
  }
  for (let elem in set) {
    result.push(set[elem]);
  }
  return result;
};
