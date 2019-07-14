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
var preorderTraversal = function(root, output = []) {
  if (root !== null) {
    output.push(root.val);
  } else {
    return [];
  }
  if (root.left && root.left !== null) {
    preorderTraversal(root.left, output);
  }
  if (root.right && root.right !== null) {
    preorderTraversal(root.right, output);
  }
  return output;
};
