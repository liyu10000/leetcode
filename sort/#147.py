# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        # create one additional node to avoid edge conditions
        cap_head = ListNode(None)
        while head:
            curr_next = head.next
            node = cap_head
            while node.next and node.next.val <= head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = curr_next
        return cap_head.next