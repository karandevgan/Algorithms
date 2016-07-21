# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        # import pdb
        # pdb.set_trace()
        length = 0
        start = A
        while start is not None:
            length += 1
            start = start.next
        mid = length / 2
        if length % 2 != 0:
            mid += 1
        
        start = A
        for _ in xrange(mid-1):
            start = start.next
        

        # This is new head
        prev = start
        
        # Reverse list starting from here
        start = start.next
        
        new = None
        while start is not None:
            temp_start = start.next
            start.next = new
            new = start
            start = temp_start
        prev.next = new
        
        i = A
        j = prev.next
        while j is not None:
            if i.val != j.val:
                return 0
            i = i.next
            j = j.next
        return 1

node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(2)
# node5 = ListNode(2)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
sol = Solution()
print sol.lPalin(node1)