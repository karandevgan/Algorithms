import pdb
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        length = self.getLength(A)
        if length == 1 or length == 0:
            return A
        
        mid = length / 2
        mid_node = A
        
        for i in xrange(mid-1):
            mid_node = mid_node.next
        
        node1 = A
        node2 = mid_node.next
        mid_node.next = None

        # LinkedList.printLinkedList(node1)
        # LinkedList.printLinkedList(node2)
        
        tempA = self.sortList(node1)
        tempB = self.sortList(node2)

        return self.merge(tempA, tempB)
    
    def getLength(self, A):
        length = 0
        while A is not None:
            length += 1
            A = A.next
        return length

    def merge(self, A, B):
        C = LinkedList.ListNode("dummy")
        head = C
        if A is None:
            return B
        elif B is None:
            return A

        while A is not None and B is not None:
            if A.val < B.val:
                C.next = A
                A = A.next
            else:
                C.next = B
                B = B.next
            C = C.next
        
        while A is not None:
            C.next = A
            A = A.next
            C = C.next
        
        while B is not None:
            C.next = B
            B = B.next
            C = C.next
        
        return head.next

import LinkedList
A = LinkedList.getRandomLinkedList(13,20)
LinkedList.printLinkedList(A)

C = Solution().sortList(A)

LinkedList.printLinkedList(C)