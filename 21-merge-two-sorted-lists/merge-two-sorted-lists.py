# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        a=list1
        b=list2
        while a and b:
            if a.val<=b.val:
                newnode=ListNode(a.val)
                curr.next=newnode
                curr=curr.next
                a=a.next
            else:
                newnode=ListNode(b.val)
                curr.next=newnode
                curr=curr.next
                b=b.next
        if a:
            curr.next=a
        if b:
            curr.next=b
        return dummy.next
