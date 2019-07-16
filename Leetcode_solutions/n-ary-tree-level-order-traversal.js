/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */
/**
 * @param {Node} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  if (root === null) {
    return [];
  }
  output = [[root.val]];
  height = 1;
  search(root.children, height, output);
  return output;
};
function search(r, h, o) {
  if (r === null) {
    return o;
  }
  if (o.length <= h && r.length > 0) {
    o.push([]);
  }
  for (let i = 0; i < r.length; i++) {
    o[h].push(r[i].val);
    search(r[i].children, h + 1, o);
  }
}
