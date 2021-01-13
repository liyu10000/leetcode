class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        prev, curr = head, head
        start = True
        while curr:
            # keep m nodes
            c = 0
            if start:
                c = 1
                start = False
            while curr and c < m:
                prev.next = curr.next
                prev = prev.next
                curr = curr.next
                c += 1
            # skip n nodes
            s = 0
            while curr and s < n:
                curr = curr.next
                s += 1
        if prev:
            prev.next = None
        return head


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        prev, curr = head, head
        while curr:
            # keep m nodes
            c = 0
            while curr and c < m:
                prev = curr
                curr = curr.next
                c += 1
            # skip n nodes
            s = 0
            while curr and s < n:
                curr = curr.next
                s += 1
            prev.next = curr
        return head