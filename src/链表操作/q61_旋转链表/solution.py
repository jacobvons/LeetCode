# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        def getLength(l: ListNode):
            if not l:
                return 0
            else:
                return 1 + getLength(l.next)
        
        def rotateOnce(l: ListNode):
            prev, curr = None, head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            return curr
        
        
        if not head or not head.next:
            return head
        else:
            time = k % getLength(head)
            
            for i in range(time):
                head = rotateOnce(head)
            return head
