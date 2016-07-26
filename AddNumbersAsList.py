import pdb
import LinkedList
from LinkedList import ListNode

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        #pdb.set_trace()
        A = self.reverseLinkedList(A)
        B = self.reverseLinkedList(B)
        if A is None:
            return B
        elif B is None:
            return A
        sum = A.val + B.val
        carry = sum / 10
        C = ListNode(sum % 10)
        returnHead = C
        A = A.next
        B = B.next
        
        while A is not None and B is not None:
            sum = A.val + B.val + carry
            carry = sum / 10
            C.next = ListNode(sum % 10)
            C = C.next
            A = A.next
            B = B.next
        
        while A is not None:
            sum = A.val + carry
            carry = sum / 10
            C.next = ListNode(sum % 10)
            C = C.next
            A = A.next

        while B is not None:
            sum = B.val + carry
            carry = sum / 10
            C.next = ListNode(sum % 10)
            C = C.next
            B = B.next
        
        if carry != 0:
            C.next = ListNode(carry)

        return returnHead
    
    def reverseLinkedList(self, A):
        prev = None
        while A is not None:
            temp = A.next
            A.next = prev
            prev = A
            A = temp
        return prev


A = LinkedList.getRandomLinkedList(3)
B = LinkedList.getRandomLinkedList(5)
LinkedList.printLinkedList(A)
LinkedList.printLinkedList(B)

sol = Solution()
C = sol.addTwoNumbers(A,B)
LinkedList.printLinkedList(C)