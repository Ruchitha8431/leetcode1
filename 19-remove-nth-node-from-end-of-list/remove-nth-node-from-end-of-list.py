# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        while n:
            fast=fast.next
            n-=1
        while fast :
             slow=slow.next
             fast=fast.next
        print(slow.val)
        if slow.next:
            slow.next=slow.next.next
        else:
            return None
        return dummy.next