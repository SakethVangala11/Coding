# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res=[]
        while(head):
            res.append(head.val)
            head = head.next
        i=0
        j=len(res)-1
        while(i<=j):
            if res[i]==res[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        