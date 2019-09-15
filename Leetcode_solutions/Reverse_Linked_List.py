# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        print(prev)
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        queue = []
        self.stock(head, queue)
        self.reverse(head, queue)
        return head

    def stock(self, h, q):
        if h == None:
            return q
        q.append(h.val)
        self.stock(h.next, q)

    def reverse(self, h, q):
        if h == None:
            return h
        h.val = q[len(q) - 1]
        q.pop()
        self.reverse(h.next, q)
