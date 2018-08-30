/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
  const result = [];
  const recursive = (node) => {
    if (node) {
      result.push(node.val);
      return recursive(node.next);
    } else {
      return result;
    }
  };
  return check(recursive(head));
};
const check = (list) => {
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    if (list[i] !== list[j]) return false;
    j--;
  }
  return true;
};
