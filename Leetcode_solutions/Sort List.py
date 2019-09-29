# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        dummyHead = ListNode(0)
        head = dummyHead
        while len(nums) > 0:
            now = nums.pop(0)
            head.next = ListNode(now)
            head = head.next
        return dummyHead.next
