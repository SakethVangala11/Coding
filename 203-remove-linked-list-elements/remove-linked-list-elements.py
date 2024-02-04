# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        current = head
        while(current):
            if current.val==val:
                current = current.next
            else:
                if not prev:
                    head = current
                else:
                    prev.next = current
                prev = current
                current = current.next
        if prev:
            prev.next = current
            return head
        else:
            return None
        
        