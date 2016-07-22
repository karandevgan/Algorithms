import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n:
            return A

        head = None
        m_is_start = (m == 1)
        if m != 1:
            head = A
        start = A
        dummy_head = None
        while m != 1:
            if m == 2:
                # Node to which reversed list has to be joined
                dummy_head = start
            start = start.next
            m -= 1
            n -= 1
        # Node form which list has to be reversed
        prev_start = start
        prev = None
        while n != 0:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
            n -= 1
        # Join the current node to the next of the node from which list was reversed
        prev_start.next = start

        # If whole list is reversed
        if head == None:
            head = prev
        else:
            dummy_head.next = prev
        
        return head
        

A = LinkedList.getRandomLinkedList(10)
LinkedList.printLinkedList(A)
sol = Solution()
head = sol.reverseBetween(A, 6,9)
LinkedList.printLinkedList(head)