# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # split list into two segments
        slow, fast = head, head
        pre = None # used to set end for the first segment
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        
        # sort separately
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # merge two lists
        cap_head = ListNode(None)
        curr = cap_head
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        curr.next = left if left else right
        
        return cap_head.next