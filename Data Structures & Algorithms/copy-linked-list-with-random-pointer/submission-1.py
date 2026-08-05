"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        org=head
        link={}
        dummy=Node(0)
        dummy.next=None
        tail=dummy
        while org:
            copy=Node(org.val)
            link[org]=copy
            tail.next=copy
            tail=copy
            org=org.next
        org=head
        while org:
            copy=link[org]
            copy.random = link.get(org.random)
            org=org.next
        return dummy.next

            



        