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
        if not head:
            return None

        dummy = node = Node(0)
        iterr = head

        soft_deep = {}
        while iterr:
            soft_deep[iterr] = Node(iterr.val)
            iterr = iterr.next

        iterr = head

        while iterr:
            tmp = soft_deep.get(iterr)
            tmp.next = soft_deep.get(iterr.next, None)
            tmp.random = soft_deep.get(iterr.random, None)
            node.next = tmp
            node = node.next
            iterr = iterr.next
        
        return dummy.next
        
