/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
  const height = 0,
    output = [];
  search(root, height, output);

  return output;
};
function search(r, h, o) {
  if (r === null) {
    return;
  }

  if (h >= o.length) {
    o.push([]);
  }

  o[h].push(r.val);
  search(r.left, h + 1, o);
  search(r.right, h + 1, o);

  return o;
}
