# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1start = list1
        l1end = list1
        l2start = list2
        l2end = list2
        count = 0
        while(True):
            if count < a-1:
                l1start = l1start.next
            if count <= b:
                l1end = l1end.next
            
            if count > a-1 and count >= b:
                break
            count+=1
        while(l2end.next):
            l2end = l2end.next
        l1start.next = l2start
        l2end.next = l1end

        return list1

        