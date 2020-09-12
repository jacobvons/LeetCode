# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        total = ListNode()
        current = total
        
        while l1 != None or l2 != None or carry != 0:
            num_a = 0 if not l1 else l1.val
            num_b = 0 if not l2 else l2.val
            sum = num_a + num_b + carry
            carry = int(sum / 10)
            current.next = ListNode(sum % 10)
            current = current.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
            
        return total.next
            
