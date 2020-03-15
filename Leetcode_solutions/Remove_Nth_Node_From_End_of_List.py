# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first != None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(1, n + 2):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 1
        current = head
        currentHead = head
        while current.next != None:
            counter += 1
            current=current.next
        targetIndex = counter - n + 1
        if targetIndex != 1:
            while targetIndex > 2:
                targetIndex -=1
                currentHead = currentHead.next
            currentHead.next = currentHead.next.next
        else:
            head=head.next
        return head