# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or k > l:
            return head
        prev, curr = None, head
        for _ in range(k):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        head.next = self.reverseKGroup(curr, k)
        return prev
