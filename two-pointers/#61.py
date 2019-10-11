# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        fast = head
        i = 0
        while fast:
            fast = fast.next
            i += 1
        if i <= k:
            k %= i
            if k == 0:
                return head
        
        slow, fast = head, head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        
        return head