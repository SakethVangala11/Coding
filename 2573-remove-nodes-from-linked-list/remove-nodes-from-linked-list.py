# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNodes(self, head):
        prev = None
        while(head):
            nxt = head.next
            head.next = prev 
            prev = head
            head = nxt
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev1 = self.reverseNodes(head)
        temp = rev1
        maxi = -1
        prev = ListNode(0,rev1)
        while(temp):
            if temp.val >= maxi:
                maxi = max(maxi, temp.val)
                temp = temp.next
                prev = prev.next
            else:
                prev.next = temp.next
                temp = prev.next
        rev2 = self.reverseNodes(rev1)
        return rev2
            
        
        