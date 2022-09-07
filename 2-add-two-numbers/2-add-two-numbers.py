# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, root, item): 
        temp = ListNode(0) 
        temp.val = item 
        temp.next = root 
        root = temp
        return root 
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = '', ''
        while l1:
            a = str(l1.val) + a
            l1 = l1.next
        while l2:
            b = str(l2.val) + b
            l2 = l2.next
        c = str(int(a) + int(b))
        root = None
        for i in c:
            root = self.insert(root, int(i))
        return root 
        