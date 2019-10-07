# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head

        tracker = head
        while tracker != None and tracker.val == head.val:
            tracker = tracker.next
        return self.deleteDuplicates(tracker)
