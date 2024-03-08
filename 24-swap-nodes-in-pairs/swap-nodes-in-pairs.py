# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = ListNode(-1)
        cur = head
        nxt = head.next
        head = prev
       
        while(True):
            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            if(cur.next and cur.next.next):
                prev = cur
                cur = cur.next
                nxt = cur.next
            else:
                break
        return head.next

        
        