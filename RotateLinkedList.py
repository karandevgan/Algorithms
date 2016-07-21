import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
   def rotateRight(self, A, B):
        length = self.getLength(A)
        if length == 1:
            return A
        B = B % length
        if B == 0:
            return A
        temp = A
        for _ in xrange(length-B-1):
            temp = temp.next
        head = temp.next
        temp.next = None
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = A
        return head
    
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