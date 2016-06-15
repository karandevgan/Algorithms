import time
from SinglyLinkedList import SingleLinkedList

def alternateList1(linkedList):
    if linkedList.length < 1:
        return linkedList

    curr_node = linkedList.HEAD.next
    while (curr_node.next != None):
        linkedList.reverse(node = curr_node)
        curr_node = curr_node.next
    return linkedList

def alternateList2(linkedList):
    if linkedList.length < 1:
        return linkedList

    length_stack = linkedList.length / 2
    remaining_length = linkedList.length - length_stack
    stack = [None] * length_stack

    curr_node = linkedList.get(0)
    stack_index = 0
    returnLinkedList = SingleLinkedList()

    while (curr_node.key != None):
        if stack_index < length_stack:
            stack[stack_index] = curr_node.key
            stack_index += 1
        else:
            break
        curr_node = curr_node.next

    while(remaining_length != length_stack and curr_node.key != None):
        returnLinkedList.insert(curr_node.key)
        curr_node = curr_node.next
        remaining_length -= 1

    while (curr_node.key != None or len(stack) > 0):
        if curr_node.key != None:
            returnLinkedList.insert(curr_node.key)
            curr_node = curr_node.next
        if (len(stack) > 0):
            returnLinkedList.insert(stack.pop())

    return returnLinkedList


size = 10000
iterations = 10
total_time = 0.0

for j in xrange(iterations):
    ll = SingleLinkedList()
    for i in xrange(size,0,-1):
        ll.insert(i)
    start_time = time.time()
    alternateList1(ll)
    end_time = time.time()
    total_time += end_time - start_time
print total_time / iterations

total_time = 0.0

for j in xrange(iterations):
    ll = SingleLinkedList()
    for i in xrange(size,0,-1):
        ll.insert(i)
    start_time = time.time()
    alternateList2(ll)
    end_time = time.time()
    total_time += end_time - start_time
print total_time / iterations
