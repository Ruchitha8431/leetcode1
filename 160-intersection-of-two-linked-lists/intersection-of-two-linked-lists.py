# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        c=0
        while a!=b:
            a=a.next
            b=b.next
            if a==None:
                a=headB
                c+=1
            if b==None:
                b=headA
            if c>2:
                return None
        return a