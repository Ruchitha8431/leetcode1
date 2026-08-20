# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=l1
        b=l2
        dummy=ListNode(0)
        curr=dummy
        sum=0
        carry=0
        while a and b:
            sum=a.val+b.val+carry
            if sum>9:
                newnode=ListNode(sum%10)
                carry=1
            else:
                newnode=ListNode(sum)
                carry=0
            curr.next=newnode
            curr=curr.next
            a=a.next
            b=b.next
        while a:
            sum=a.val+carry
            if sum>9:
                newnode=ListNode(sum%10)
                carry=1
            else:
                newnode=ListNode(sum)
                carry=0
            curr.next=newnode
            curr=curr.next
            a=a.next
        while b:
            sum=b.val+carry
            if sum>9:
                newnode=ListNode(sum%10)
                carry=1
            else:
                newnode=ListNode(sum)
                carry=0
            curr.next=newnode
            curr=curr.next
            b=b.next
        if carry:
            curr.next=ListNode(1)
        return dummy.next
