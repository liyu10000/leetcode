# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head, curr = None, None,
        while l1 is not None and l2 is not None:
            val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            if head is None:
                head = ListNode(val)
                curr = head
            else:
                curr.next = ListNode(val)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        if l1 is None:
            l1 = l2
        while l1 is not None:
            val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        
        if carry > 0:
            curr.next = ListNode(carry)
            
        return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l, cur = None, None
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            val, carry = carry % 10, carry // 10
            if l is None:
                l = ListNode(val)
                cur = l
            else:
                cur.next = ListNode(val)
                cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return l