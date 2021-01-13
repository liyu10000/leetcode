class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        while head:
            n = n << 1 | head.val
            head = head.next
        return n