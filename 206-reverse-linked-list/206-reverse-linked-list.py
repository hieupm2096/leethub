# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        while True:
            curNext = head.next
            head.next = prev
            prev = head
            head = curNext
            if head == None:
                return prev
        
        
        
#         return self.reverse(None, head)
        
#     def reverse(self, prev: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
#         if cur is None:
#             return prev
#         curNext = cur.next
#         cur.next = prev
#         return self.reverse(cur, curNext)
        