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
var isBalanced = function(root) {
  //     compute the depth of left and right
  //     compare the difference if it is bigger than 1
  //     if it is bigger, return false otherwise true
  if (!root) return true;
  const left = compute(root.left),
    right = compute(root.right),
    difference = Math.abs(left - right);
  let result = true;
  console.log(left, right);
  if (difference >= 2) result = false;
  return result && isBalanced(root.left) && isBalanced(root.right);
};
const compute = (node) => {
  if (node === null) return 0;
  return 1 + Math.max(compute(node.left), compute(node.right));
};
