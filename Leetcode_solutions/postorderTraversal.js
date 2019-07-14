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
var postorderTraversal = function(root, output = []) {
  if (root === null) {
    return [];
  }
  if (root.left && root.left !== null) {
    postorderTraversal(root.left, output);
  }
  if (root.right && root.right !== null) {
    postorderTraversal(root.right, output);
  }
  if (root !== null) {
    output.push(root.val);
  } else {
    return [];
  }
  return output;
};
