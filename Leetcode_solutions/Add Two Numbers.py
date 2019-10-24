# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0) 
        # dummy.next = None
        head = dummy
        # dummy=head
        # dummy.next=head
        while (l1 != None or l2 != None) or carry>0:
            l1v = 0
            l2v = 0
            if l1 != None:
                l1v = l1.val
                l1 = l1.next
            if l2 != None:
                l2v = l2.val
                l2 = l2.next
            total = l1v + l2v + carry
            if total>=10:
                newNode = ListNode(total%10)
                carry=1
            else:
                newNode = ListNode(total)
                carry=0
            head.next = newNode
            head = head.next
        return dummy.next
            