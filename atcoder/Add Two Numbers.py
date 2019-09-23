# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        vals = []
        while l1 or l2:
            if l1:
                l1v = l1.val
                l1 = l1.next
            else:
                l1v = 0
            if l2:
                l2v = l2.val
                l2 = l2.next
            else:
                l2v = 0
            total = l1v + l2v + carry
            if total >= 10:
                total = total - 10
                carry = 1
            else:
                carry = 0
            vals.append(total)
        if carry > 0:
            vals.append(carry)
        dummy = ListNode(0)
        head = dummy
        while len(vals) > 0:
            now = vals.pop(0)
            head.next = ListNode(now)

            head = head.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if (l1 != None) else 0
            y = l2.val if (l2 != None) else 0
            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if (l1 != None) else 0
            y = l2.val if (l2 != None) else 0
            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next
