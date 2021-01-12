# save values, O(n) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


# reverse second half and compare
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find half point
        half = self.findHalf(head)
        # self.printList(half)
        
        # reverse the second half
        half = self.reverseList(half)
        # self.printList(half)
        # self.printList(head)
        
        # check first half and reversed second half
        while head and half:
            if head.val != half.val:
                return False
            head = head.next
            half = half.next
        return True
    
    def findHalf(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            tmpnext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpnext
        return prev

    def printList(self, head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        print(vals)