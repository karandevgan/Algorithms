class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A is None or A.next is None:
            return A
        
        head = LinkedList.ListNode("dummy")
        head.next = A
        # Stores the starting element
        pointer1 = head.next

        # Stores the candidate
        pointer2 = pointer1.next

        # Stores the pointer before candidate
        pointer3 = pointer1

        prev = head
        # import pdb
        # pdb.set_trace()
        while pointer2 is not None:
            while pointer1.val < pointer2.val:
                prev = pointer1
                pointer1 = pointer1.next
            if pointer1 != pointer2:
                pointer3.next = pointer2.next
                prev.next = pointer2
                pointer2.next = pointer1
            else:
                pointer3 = pointer2
            pointer1 = head.next
            prev = head
            pointer2 = pointer3.next
        return head.next

import LinkedList

A = LinkedList.getRandomLinkedList(3,20)
LinkedList.printLinkedList(A)
sol = Solution()
LinkedList.printLinkedList(sol.insertionSortList(A))