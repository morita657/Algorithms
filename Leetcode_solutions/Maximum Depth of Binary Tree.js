var maxDepth = function(root) {
  if (!root) return 0;
  let max = 0;
  function dfs(node, level) {
    if (node.left) {
      dfs(node.left, level + 1);
    }
    if (node.right) {
      dfs(node.right, level + 1);
    } else {
      max = Math.max(max, level);
    }
  }
  dfs(root, 1);
  return max;
};
