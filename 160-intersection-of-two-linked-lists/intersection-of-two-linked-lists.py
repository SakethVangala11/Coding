# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        while(headA):
            if headA not in s:
                s.add(headA)
            else:
                return headA
            headA=headA.next
        while(headB):
            if headB not in s:
                s.add(headB)
            else:
                return headB
            headB=headB.next
        return None
        