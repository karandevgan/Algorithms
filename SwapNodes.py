import pdb

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        start = LinkedList.ListNode("dummy")
        start.next = A
        current = start

        while current.next and current.next.next:
            current.next = self.swapNodes(current.next, current.next.next)
            current = current.next.next
        return start.next
    
    def swapNodes(self, A, B):
        A.next = B.next
        B.next = A
        return B

import LinkedList
A = LinkedList.getRandomLinkedList(11, 20)
LinkedList.printLinkedList(A)
sol= Solution()
B = sol.swapPairs(A)
LinkedList.printLinkedList(B)