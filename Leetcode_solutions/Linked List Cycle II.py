# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        node = head
        while node != None:
            if node in seen:
                return node
            else:
                seen.add(node)
                node = node.next
        return None
