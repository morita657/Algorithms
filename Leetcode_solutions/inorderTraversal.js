/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root, output = []) {
  if (root === null) {
    return [];
  }
  if (root.left && root.left !== null) {
    inorderTraversal(root.left, output);
  }
  if (root !== null) {
    output.push(root.val);
  } else {
    return [];
  }
  if (root.right && root.right !== null) {
    inorderTraversal(root.right, output);
  }
  return output;
};
