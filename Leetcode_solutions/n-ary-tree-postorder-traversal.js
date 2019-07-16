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
var postorder = function(root) {
  if (root === null) {
    return [];
  }
  output = [];
  search(root.children, output);
  output.push(root.val);
  return output;
};

function search(r, o) {
  for (let i = 0; i < r.length; i++) {
    if (r[i].children.length === 0) {
      o.push(r[i].val);
    } else {
      search(r[i].children, o);
      o.push(r[i].val);
    }
  }
  return o;
}
