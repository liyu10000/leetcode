# reverse and add
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbers1(l1, l2))
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
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


# add and reverse
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # get length and swap lists
        n1 = self.getLength(l1)
        n2 = self.getLength(l2)
        if n2 > n1:
            n1, n2 = n2, n1
            l1, l2 = l2, l1
        # add corresponding digits, without carry
        l, c = None, None
        for _ in range(n1 - n2):
            if l is None:
                l = ListNode(l1.val)
                c = l
            else:
                c.next = ListNode(l1.val)
                c = c.next
            l1 = l1.next
        for _ in range(n2):
            if l is None:
                l = ListNode(l1.val + l2.val)
                c = l
            else:
                c.next = ListNode(l1.val + l2.val)
                c = c.next
            l1 = l1.next
            l2 = l2.next
        l = self.reverseList(l)
        # print(l)
        # update with carry
        carry = 0
        prev, curr = None, l
        while curr:
            if curr.val + carry > 9:
                carry, curr.val = (curr.val + carry) // 10, (curr.val + carry) % 10
            else:
                carry, curr.val = 0, curr.val + carry
            prev = curr
            curr = curr.next
            if curr is None and carry > 0:
                prev.next = ListNode(carry)
                break
        l = self.reverseList(l)
        # print(l)
        return l
        
    def getLength(self, l):
        n = 0
        while l:
            n += 1
            l = l.next
        return n
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nextTmp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTmp
        return prev