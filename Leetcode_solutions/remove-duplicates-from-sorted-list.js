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
var deleteDuplicates = function(head) {
  curr = head;
  while (curr !== null) {
    while (curr.next !== null && curr.val === curr.next.val) {
      curr.next = curr.next.next;
    }
    curr = curr.next;
  }
  return head;
};
