"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # Step 1
        temp = head
        while temp:
            new_node = Node(x=temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next
            
        # Step 2
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Step 3
        new_head = head.next
        new_p = new_head
        old_p = head
        while new_p.next:
            old_p.next = new_p.next
            old_p = old_p.next
            new_p.next = old_p.next
            new_p = new_p.next
        old_p.next = None
        new_p.next = None
        return new_head
