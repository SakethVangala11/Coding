# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1,c2=0,0
        l1=headA
        l2=headB
        while(headA):
            c1+=1
            headA=headA.next
        while(headB):
            c2+=1
            headB=headB.next
        if c2>c1:
            diff=c2-c1
            while(l2):
                if diff:
                    l2=l2.next
                    diff-=1
                else:
                    break
        else:
            diff=c1-c2
            while(l1):
                if diff:
                    l1=l1.next
                    diff-=1
                else:
                    break
        while(l1 and l2):
            if l1==l2:
                return l1
            else:
                l1=l1.next
                l2=l2.next
        return None



        