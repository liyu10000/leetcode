# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        large = ListNode(0)
        tmp_s = small
        tmp_l = large
        while head:
            if head.val < x:
                tmp_s.next = head
                tmp_s = tmp_s.next
            else:
                tmp_l.next = head
                tmp_l = tmp_l.next
            head = head.next
        tmp_s.next = large.next
        tmp_l.next = None
        return small.next