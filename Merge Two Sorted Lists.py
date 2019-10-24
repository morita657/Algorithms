# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        while l1 != None or l2 != None:
            l1v = float('inf')
            l2v = float('inf')
            if l1 != None:
                l1v = l1.val
            if l2 != None:
                l2v = l2.val
            if l1v<=l2v:
                head.next = ListNode(l1v)
                l1=l1.next
            else:
                head.next = ListNode(l2v)
                l2=l2.next
            head = head.next
        return dummy.next
            