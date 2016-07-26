import LinkedList

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        length = self.getLength(A)
        mid = length / 2
        start = A
        for i in xrange(mid-1):
            start = start.next
        prev = start
        start = start.next
        prev.next = self.reverseList(start)
        start1 = A
        head = start1
        start2 = prev.next
        for i in xrange(mid-1):
            temp =  start1.next
            prev.next = start2.next
            start2.next = temp
            start1.next = start2
            start1 = temp
            start2 = prev.next
        return head
        
    
    def getLength(self, A):
        length = 0
        while A is not None:
            A = A.next
            length += 1
        return length

    def reverseList(self, A):
        prev = None
        while A is not None:
            temp = A.next
            A.next = prev
            prev = A
            A = temp
        return prev

sol = Solution()
A = LinkedList.getRandomLinkedList(10)
LinkedList.printLinkedList(A)
LinkedList.printLinkedList(sol.reorderList(A))
