/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  const nodeVals = [];
  search(head, nodeVals);
  let index = 0;
  nodeVals.reverse();
  return nodeVals;
};

const search = (node, nodeVals = []) => {
  if (node) {
    nodeVals.push(node.val);
    search(node.next, nodeVals);
  } else {
    return nodeVals;
  }
};
