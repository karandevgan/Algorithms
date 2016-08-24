# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dict_nodes = {}
        original_node = head
        while original_node is not None:
            tempNode = RandomListNode(original_node.label)
            dict_nodes[original_node] = tempNode
            original_node = original_node.next
        
        original_node = head
        while original_node is not None:
            dict_nodes.get(original_node).next = dict_nodes.get(original_node.next)
            dict_nodes.get(original_node).random = dict_nodes.get(original_node.random)
            original_node = original_node.next
        
        return dict_nodes.get(head)