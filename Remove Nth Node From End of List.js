/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  //     read until the last element
  const computeDepth = (node, level) => {
    if (node && node.next) {
      return computeDepth(node.next, level + 1);
    }
    return level;
  };
  //     find the depth
  const maxDepth = computeDepth(head, 1);
  //     handle edge cases
  if (maxDepth <= 1 && n <= 1) {
    return [];
  }
  if (maxDepth === n) {
    return head.next;
  }
  //     compute the target value. target value is in front of value n. In case of the example, it's 3
  const target = maxDepth - n;
  //     finding the target, connect the next property as next.next
  let currentDepth = 1;
  const findTarget = (node, val) => {
    if (val === target) {
      node.next = node.next.next;
      return node;
    } else {
      return findTarget(node.next, val + 1);
    }
  };
  findTarget(head, 1);
  //     return head
  return head;
};
