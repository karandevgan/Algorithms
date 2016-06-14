import time
from SinglyLinkedList import SingleLinkedList

def alternateList1(linkedList):
    if linkedList.length < 1:
        return linkedList

    for i in xrange(1, linkedList.length):
        linkedList.reverse(i)

    return linkedList

def alternateList2(linkedList):
    if linkedList.length < 1:
        return linkedList

    length_queue = linkedList.length / 2
    length_stack = linkedList.length - length_queue
    queue = [None] * length_queue
    stack = [None] * length_stack

    curr_node = linkedList.get(0)
    queue_index = 0
    stack_index = 0
    returnLinkedList = SingleLinkedList()

    while (curr_node.key != None):
        if queue_index < length_queue:
            queue[queue_index] = curr_node.key
            queue_index += 1
        else:
            stack[len(stack) - 1 - stack_index] = curr_node.key
            stack_index += 1
        curr_node = curr_node.next

    while (len(queue) > 0 or len(stack) > 0):
        if (len(stack) > 0):
            returnLinkedList.insert(stack.pop())
        if (len(queue) > 0):
            returnLinkedList.insert(queue.pop())
    return returnLinkedList


ll = SingleLinkedList()
size = 10000
for i in xrange(size,0,-1):
    ll.insert(i)
start_time = time.time()
alternateList1(ll)
end_time = time.time()
print end_time - start_time

ll = SingleLinkedList()
for i in xrange(size,0,-1):
    ll.insert(i)
start_time = time.time()
alternateList2(ll)
end_time = time.time()
print end_time - start_time
