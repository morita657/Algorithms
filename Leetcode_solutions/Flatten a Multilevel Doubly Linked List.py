"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        stack = [head]
        new_head = head 
        cur = new_head  
        
        while(stack):
            cur_node = stack.pop()
            if cur_node.next:
                stack.append(cur_node.next) 
            if cur_node.child:
                stack.append(cur_node.child) # append child node before next, s.t. child node will appear first while popping.
            cur_node.child = None # remember to set child to None, since we now have a linear linked list
            cur_node.prev = cur
            cur.next = cur_node
            cur = cur.next

        new_head.prev = None # remember to make sure new_head's prev is None
        return new_head
 









 """
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
		if not head:
			new_node.next = new_node
			return new_node

		cur = head

		while not (cur.val < insertVal <= cur.next.val):

			# cur is max, and cur.next is min. If max < v or min >= v, we stop
			if cur.next.val <= cur.val:
				if cur.val < insertVal or cur.next.val >= insertVal:
					break

			cur = cur.next

		new_node.next, cur.next = cur.next, new_node
		return head