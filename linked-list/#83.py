# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursive
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        def moveon(node):
            if node is None:
                return node
            if node.val in a:
                return moveon(node.next)
            else:
                a.add(node.val)
                node.next = moveon(node.next)
                return node
            
        a = set()
        return moveon(head)

# iterative
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        slow, fast = head, head.next
        while fast:
            if slow.val < fast.val:
                slow = slow.next
                fast = fast.next
            else:
                slow.next = fast.next
                fast = slow.next
        return head