# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, post = head, head
        for i in range(n):
            pre = pre.next
        # consider the case when n equals the length of the list
        if pre is None:
            return head.next
        while pre.next:
            pre = pre.next
            post = post.next
        post.next = post.next.next
        return head