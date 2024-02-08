# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while(fast):
            slow = slow.next
            fast = fast.next.next
        
        c=slow.next
        prev=None
        while(c):
            slow.next = prev
            prev =slow
            slow = c
            c = slow.next
        slow.next = prev
        maxi=-1
        while(head and slow):
            if head.val+slow.val > maxi:
                maxi = head.val + slow.val
            head = head.next
            slow = slow.next
        return maxi
        


        