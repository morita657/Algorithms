public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null
        ListNode odd = head, even = head.next, evenHead = even
        while (even != null & & even.next != null) {
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        }
        odd.next = evenHead
        return head
    }
}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
