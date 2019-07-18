/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var lca,
  deepest = 0;
var lcaDeepestLeaves = function(root) {
  height = 0;
  search(root, height);
  return lca;
};
function search(r, level) {
  deepest = Math.max(deepest, level);
  if (r === null) {
    return lca;
  }
  left = search(r.left, level + 1);
  right = search(r.right, level + 1);
  if (left === deepest && right === deepest) {
    lca = r;
  }
  return Math.max(left, right);
}
