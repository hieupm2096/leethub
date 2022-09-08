# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversedNode(self, head: Optional[ListNode]) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next
        return slow
    
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while head:
            cur = head.next
            head.next = prev
            prev = head
            head = cur
        return prev
            
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversedNode = self.reversedNode(head)
        tail = self.reverse(reversedNode)
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
        