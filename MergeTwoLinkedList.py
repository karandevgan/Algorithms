import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        C = None
        head = None
        smaller = None
        while A is not None and B is not None:
            if A.val < B.val:
                smaller = A
                A = A.next
            else:
                smaller = B
                B = B.next

            if C is None:
                head = smaller
                C = smaller
            else:
                C.next = smaller
                C = C.next
        

        nonEmpty = None
        if A is not None:
            nonEmpty = A
        elif B is not None:
            nonEmpty = B

        while nonEmpty is not None:
            if C is None:
                C = nonEmpty
                head = nonEmpty
            else:
                C.next = nonEmpty
                C = C.next
            nonEmpty = nonEmpty.next
        
        return head

A = LinkedList.getSortedLinkedList(10)
LinkedList.printLinkedList(A)
B = LinkedList.getSortedLinkedList(1)
LinkedList.printLinkedList(B)
sol = Solution()
C = sol.mergeTwoLists(A,B)
LinkedList.printLinkedList(C)