# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev=head
        current=head.next
        while(current):
            if prev.val==current.val:
                current=current.next
            else:
                prev.next=current
                prev=current
                current=current.next
        prev.next=current
        return head
        