# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def merge(self,head1, head2):
        dummy=ListNode()
        dummy.next=None
        tail=dummy
        while head1 and head2:
            if head1.val<=head2.val:
                tail.next=head1
                head1=head1.next
            else:
                tail.next=head2
                head2=head2.next
            tail=tail.next
        if head1:
            tail.next=head1
        elif head2:
            tail.next=head2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        if len(lists)==1:
            return lists
        interval=1
        while interval < len(lists):
            i=0
            while i+interval<len(lists):
                lists[i] = self.merge(lists[i],lists[i + interval])
                i+=interval*2
            interval *= 2
        return lists[0]