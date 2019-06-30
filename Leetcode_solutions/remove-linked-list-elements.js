/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var getNext = function(head, val) {
  let next = head;
  while (next && next.val === val) {
    next = next.next;
  }
  return next;
};

var removeElements = function(head, val) {
  head = getNext(head, val);
  let start = head,
    prev = head,
    next;
  while (prev) {
    next = prev.next;
    next = getNext(next, val);
    prev.next = next;
    prev = next;
  }
  return start;
};
console.log(removeElements([1, 2, 6, 3, 4, 5, 6], 6));
