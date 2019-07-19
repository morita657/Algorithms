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
  if (root === null) return true;
  (r = []), (l = []);
  if (root.left !== null && root.right === null) {
    return false;
  } else if (root.left === null && root.right !== null) {
    return false;
  } else {
    left = search(root.left, l, "left");
    right = search(root.right, r, "right");
  }
  if (left.length === right.length) {
    for (let i = 0; i < left.length; i++) {
      if (left[i] !== right[i]) {
        return false;
      }
    }
    return true;
  }
  return false;
};

function search(r, output, flag) {
  if (r === null) {
    output.push("");
  } else {
    output.push(r.val || "");
    if (flag == "left") {
      search(r.left, output, "left");
      search(r.right, output, "right");
    } else {
      search(r.right, output, "right");
      search(r.left, output, "left");
    }
  }
  return output;
}
