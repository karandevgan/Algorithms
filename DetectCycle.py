class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow_pointer = A
        fast_pointer = A
        while True:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer is None or fast_pointer.next is None:
                return None
            
            fast_pointer = fast_pointer.next
            if fast_pointer == slow_pointer:
                slow_pointer = A
                return self.getLoopNode(slow_pointer, fast_pointer)

    def getLoopNode(self, slow_pointer, fast_pointer):
        while (slow_pointer != fast_pointer):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return fast_pointer