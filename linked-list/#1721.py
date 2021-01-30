class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # find length of list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        # find two nodes
        node1, node2 = None, None
        curr = head
        for i in range(n):
            if i == k-1:
                node1 = curr
            if i == n-k:
                node2 = curr
            curr = curr.next
        # swap values
        node1.val, node2.val = node2.val, node1.val
        return head

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        k1, k2 = head, head
        curr = head
        for _ in range(k-1):
            curr = curr.next
        k1 = curr
        while curr.next:
            curr = curr.next
            k2 = k2.next
        k1.val, k2.val = k2.val, k1.val
        return head