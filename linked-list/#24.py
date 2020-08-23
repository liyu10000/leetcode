# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursive solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        curr = head
        head = head.next
        curr.next = head.next
        head.next = curr
        head.next.next = self.swapPairs(head.next.next)
        return head

# iterative solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = next_head = ListNode(0)
        dummy.next = head
        cur = head
        while cur and cur.next:
            first = cur
            second = cur.next
            
            # swap
            next_head.next = second   # update the head pointer
            first.next = second.next
            second.next = first
            
            # update next_head and cur node for next swap
            next_head = first
            cur = first.next
            
        return dummy.next