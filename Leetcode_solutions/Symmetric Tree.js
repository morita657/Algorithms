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
  if (!root) {
    // Sanity check
    return true;
  }

  function isMirror(s, t) {
    var q1 = [s],
      q2 = [t];

    // Perform breadth-first search
    while (q1.length > 0 || q2.length > 0) {
      // Dequeue
      var n1 = q1.shift(),
        n2 = q2.shift();

      // Two null nodes, let's continue
      if (!n1 && !n2) continue;

      // Return false as long as there is a mismatch
      if (!n1 || !n2 || n1.val !== n2.val) return false;

      // Scan tree s from left to right
      // and scan tree t from right to left
      q1.push(n1.left);
      q1.push(n1.right);
      q2.push(n2.right);
      q2.push(n2.left);
    }

    return true;
  }
  return isMirror(root.left, root.right);
};

console.log(isSymmetric([1, 2, 2, 3, 4, 4, 3]));
