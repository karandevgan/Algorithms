# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    def deleteDuplicates(self, A):
        # import pdb
        # pdb.set_trace()
        head = A
        splice = None
        prev = A
        next = prev.next

        while next is not None:
            isRepeat = False
            if prev.val == next.val:
                isRepeat = True
            else:
                splice = prev

            while next is not None and prev.val == next.val:
                next = next.next
            
            if isRepeat:
                if splice is None:
                    splice = next
                else:
                    splice.next = next

            if isRepeat and head.val == prev.val:
                head = next
            if next is None:
                return head
            prev = next
            next = prev.next
        return head