# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwo(lists[i], lists[i - 1])
        
        return lists[-1]

    def mergeTwo(self, list1, list2):
        start = ListNode()
        curr = start
        one = list1
        two = list2

        while one and two:
            if one.val < two.val:
                curr.next = ListNode(val = one.val)
                one = one.next
            else:
                curr.next = ListNode(val = two.val)
                two = two.next
            curr = curr.next
        
        while one:
            curr.next = ListNode(one.val)
            one = one.next
            curr = curr.next

        while two:
            curr.next = ListNode(two.val)
            two = two.next
            curr = curr.next
        
        return start.next