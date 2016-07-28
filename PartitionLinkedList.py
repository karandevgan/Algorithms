import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        start_node = LinkedList.ListNode("dummy")
        start_node.next = A
        head = start_node
        
        start_node_greater = LinkedList.ListNode("dummy")
        head_greater = start_node_greater

        while A is not None:
            if A.val >= B:
                start_node_greater.next = A
                start_node_greater = start_node_greater.next
                start_node.next = A.next
            else:
                start_node = A
            A = start_node.next
            start_node_greater.next = None   


        if head_greater.next is not None:
            start_node.next = head_greater.next

        return head.next

A = LinkedList.getRandomLinkedList(10, 20)
LinkedList.printLinkedList(A)
B = 3
sol = Solution()
LinkedList.printLinkedList(sol.partition(A,B))