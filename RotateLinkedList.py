import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        length = self.getLength(A)
        if length <= 1:
            return A
        B = B % length
        if B == 0:
            return A
        A = self.reverseList(A, length, None, None)
        tail = A
        for _ in xrange(B):
            tail = tail.next
        A = self.reverseList(A, B, None, tail)
        head = A
        for _ in xrange(B-1):
            head = head.next
        self.reverseList(head.next, length-B, head, None)
        return A

    def reverseList(self, A, B, H, T):
        next = T
        while B != 0:
            temp_next = A.next
            A.next = next
            next = A
            A = temp_next
            B -= 1
        if H is None:
            H = next
        else:
            H.next = next
        return H
    
    def getLength(self, A):
        length = 0
        while A is not None:
            length += 1
            A = A.next
        return length

sol = Solution()
A = LinkedList.getRandomLinkedList(2)
LinkedList.printLinkedList(A)
A = sol.rotateRight(A, 2)
LinkedList.printLinkedList(A)