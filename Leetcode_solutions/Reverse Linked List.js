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
  queue = [];
  stock(head, queue);
  reverse(head, queue);
  return head;
};
function stock(h, q) {
  if (h === null) {
    return q;
  }
  q.push(h.val);
  stock(h.next, q);
}
function reverse(h, q) {
  if (h === null) {
    return h;
  }
  h.val = q[q.length - 1];
  q.pop();
  reverse(h.next, q);
}
