/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
        ListNode pSlow = head;
        ListNode pFast = head == null ? head : head.next;
        while (pFast != pSlow) {
            if (pFast == null || pFast.next == null) {
                return false;
            } 
            pSlow = pSlow.next;
            pFast = pFast.next.next;
        }
        return pFast == null ? false : true;
    }
}
