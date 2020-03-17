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


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        currentHead = head
        while head.next != None:
            p = head.next
            head.next = p.next
            p.next = currentHead
            currentHead = p
        return currentHead


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        memory = []
        dummyHead = ListNode(0)
        dummyHead.next = head
        current = head
        while current != None:
            memory.append(current.val)
            current = current.next
        reversed_memory = memory[::-1]
        i=0
        while head != None:
            head.val = reversed_memory[i]
            i+=1
            head = head.next
        return dummyHead.next