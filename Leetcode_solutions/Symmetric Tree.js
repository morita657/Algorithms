/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
  return mirror(root, root);
};
const mirror = (node1, node2) => {
  if (!node1 && !node2) return true;
  if ((!node1 && node2) || (node1 && !node2)) return false;
  if (node1 && node2) {
    return (
      node1.val === node2.val &&
      mirror(node1.left, node2.right) &&
      mirror(node1.right, node2.left)
    );
  }
};
