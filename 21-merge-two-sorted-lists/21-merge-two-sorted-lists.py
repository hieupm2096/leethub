# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # store the head of merged linked list
        tail = dummy # store the last node of merged linked list
        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        return dummy.next
            
            