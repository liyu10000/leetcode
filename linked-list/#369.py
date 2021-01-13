class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head = self.reverse(head)
        # self.print(head)
        self.addOne(head)
        # self.print(head)
        return self.reverse(head)
    
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def addOne(self, head):
        carry = 1
        prev, curr = None, head
        while curr:
            val = curr.val + carry
            val, carry = val % 10, val // 10
            curr.val = val
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)
        return head
    
    def print(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        print(vals)