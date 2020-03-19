# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        rabbit = head.next
        while head:
            if rabbit == None or rabbit.next == None:
                return False
            if head.val == rabbit.val:
                return True
            head = head.next
            rabbit = rabbit.next.next
        return False
    
    def hasCycle1(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True