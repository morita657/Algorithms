/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  res = [];
  levelHelper(res, root, 0);
  return res;
};

function levelHelper(result, root, height) {
  if (root === null) return;
  console.log("height: ", height, "result: ", result.length, result);

  if (height >= result.length) {
    result.push([]);
  }
  res[height].push(root.val);
  levelHelper(result, root.left, height + 1);
  levelHelper(result, root.right, height + 1);
}
