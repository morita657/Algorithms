# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        elements = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                elements.append(head.val)
                head = head.next
        elements.sort()
        dummy = ListNode(0)
        head = dummy
        i = 0
        while i < len(elements):
            head.next = ListNode(elements[i])
            head = head.next

            i += 1
        return dummy.next
