# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        dummy = node = ListNode()

        while one and two:
            if one.val < two.val:
                node.next = one
                one = one.next
            else:
                node.next = two
                two = two.next
                
            node = node.next
            
        node.next = one or two
        
        return dummy.next