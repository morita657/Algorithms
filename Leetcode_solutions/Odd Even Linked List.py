
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddDummy = ListNode(0)
        odd = oddDummy
        evenDummy = ListNode(0)
        even = evenDummy
        i = 1
        while head:
            now = ListNode(head.val)
            if i % 2 == 0:
                even.next = now
                even = even.next
            else:
                odd.next = now
                odd = odd.next
            head = head.next
            i += 1
        odd.next = evenDummy.next
        return oddDummy.next
