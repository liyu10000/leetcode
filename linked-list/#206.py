# record values and create new node list
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        vals = []
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        vals.reverse()
        for i,val in enumerate(vals):
            if i == 0:
                head = ListNode(val)
                curr = head
            else:
                curr.next = ListNode(val)
                curr = curr.next
        return head

# swap nodes iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            tmpnext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpnext
        return prev

# swap nodes recursively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p