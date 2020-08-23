# record all nodes and check duplicates at iteration
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()
        curr = head
        while curr is not None:
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = curr.next
        return False

# two-pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while (slow != fast):
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True