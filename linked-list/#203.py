class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head