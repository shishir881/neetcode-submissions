# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=None
        tail=dummy
        first=l1
        second=l2
        carry=0
        while first or second or carry:
            if second and not first:
                esum=second.val+carry
                second=second.next
            elif first and not second:
                esum=first.val+carry
                first=first.next
            elif not first and not second:
                esum=carry
            else:
                esum=first.val+second.val+carry
                first=first.next
                second=second.next
            node_val=esum/10
            carry,node_val=divmod(esum,10)
            sumn=ListNode(node_val)
            sumn.val=node_val
            tail.next=sumn
            tail=sumn
        return dummy.next






        
        