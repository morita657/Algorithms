/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */
/**
 * @param {Node} root
 * @return {number[]}
 */
var preorder = function(root) {
  if (root === null) {
    return [];
  }
  output = [[root.val]];
  search(root.children, output);
  return output;
};
function search(r, o) {
  if (r === null) {
    return o;
  }
  for (let i = 0; i < r.length; i++) {
    o.push(r[i].val);
    search(r[i].children, o);
  }
}
