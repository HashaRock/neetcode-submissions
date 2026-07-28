# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lenlist = 0
        while curr:
            curr = curr.next
            lenlist += 1
        
        prev, curr = None, head
        for i in range(lenlist - n):
            prev = curr
            curr = curr.next

        if not prev:
            return head.next
        else:
            prev.next = curr.next
        
        return head