import LinkedList

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        prev = head
        next = A.next
        while next is not None:
            while next is not None and next.val == prev.val:
                next = next.next
            prev.next = next
            prev = prev.next
            if next is not None:
                next = next.next
        return head

A = LinkedList.getSortedLinkedList(2)
LinkedList.printLinkedList(A)
sol = Solution()
A = sol.deleteDuplicates(A)
LinkedList.printLinkedList(A)