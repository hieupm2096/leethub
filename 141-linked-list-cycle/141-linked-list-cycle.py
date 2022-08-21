# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        set_node = set()
        while head:
            if head in set_node:
                return True
            set_node.add(head)
            head = head.next
        return False
            
        