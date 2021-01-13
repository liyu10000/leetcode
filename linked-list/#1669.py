class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # find the point to insert list2
        head1 = list1
        for i in range(a-1):
            head1 = head1.next
        # find the 2nd part of list1
        tail1 = head1
        for i in range(b-a+2):
            tail1 = tail1.next
        # find the tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        # link
        head1.next = list2
        tail2.next = tail1
        return list1