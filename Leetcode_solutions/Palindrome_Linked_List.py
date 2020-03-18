# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cand = []
        while head:
            cand.append(head.val)
            head = head.next
        if len(cand) == 1:
            return True
        mid = len(cand) // 2
        if len(cand) % 2 != 0:
            return cand[:mid + 1][::-1] == cand[mid:]
        else:
            return cand[:mid][::-1] == cand[mid:]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None:
            return True
        seen = []
        while head != None:
            seen.append(head.val)
            head = head.next
        return seen == seen[::-1]