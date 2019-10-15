# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        tmp_head = ListNode(None)
        last = tmp_head
        
        curr = head
        while curr:
            found = 0
            first = curr
            first_val = curr.val
            while curr and curr.val == first_val:
                found += 1
                curr = curr.next
            if found == 1:
                last.next = first
                last = first
                
        last.next = None
        return tmp_head.next
        