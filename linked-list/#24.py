# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        curr = head
        head = curr.next
        curr.next = curr.next.next
        head.next = curr
        
        head.next.next = self.swapPairs(head.next.next)
        return head