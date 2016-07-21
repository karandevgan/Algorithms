import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if A is None:
            return A
        length = self.getLength(A)

        if B >= length or length == 1:
            A = A.next
            return A

        index_to_be_removed = length - B
        node = A
        for _ in xrange(index_to_be_removed-1):
            node = node.next
        node.next = node.next.next
        return A

    def getLength(self, A):
        length = 0
        while A is not None:
            length += 1
            A = A.next
        return length

A = LinkedList.getRandomLinkedList(10)
LinkedList.printLinkedList(A)
B = 10

sol = Solution()
A = sol.removeNthFromEnd(A,B)
LinkedList.printLinkedList(A)