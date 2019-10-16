# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# merge two lists at a time
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        while len(lists) > 1:
            lists_new = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    lists_new.append(self.merge2Lists(lists[i], lists[i+1]))
                else:
                    lists_new.append(lists[i])
            lists = lists_new
        return lists[0]
        
    def merge2Lists(self, l1, l2):
        head, curr = None, None
        while l1 and l2:
            if l1.val < l2.val:
                if head is None:
                    head = l1
                    curr = head
                else:
                    curr.next = l1
                    curr = curr.next
                l1 = l1.next
            else:
                if head is None:
                    head = l2
                    curr = head
                else:
                    curr.next = l2
                    curr = curr.next
                l2 = l2.next
        if head is None:
            head = l1 if l1 else l2
        else:
            curr.next = l1 if l1 else l2
        return head


# use heapq
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        cand = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(cand, (node.val, i, node))

        curr = guard = ListNode(None)
        while cand:
            _, i, node = heapq.heappop(cand)
            if node.next:
                heapq.heappush(cand, (node.next.val, i, node.next))
            curr, curr.next = curr.next, node

        return guard.next
