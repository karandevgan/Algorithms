class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getRandomNodes(n, top):
    import random
    nodes = []
    for i in xrange(n):
        node = ListNode(random.randint(0,top))
        nodes.append(node)
    return nodes

def joinNodes(nodes):
    for i in xrange(1,len(nodes)):
        nodes[i-1].next = nodes[i]

def getRandomLinkedList(n, top = 9):
    nodes = getRandomNodes(n, top)
    joinNodes(nodes)
    return nodes[0]

def getSortedLinkedList(n, top = 9):
    nodes = getRandomNodes(n, top)
    nodes = sorted(nodes, key=lambda x: x.val)
    joinNodes(nodes)
    return nodes[0]

def printLinkedList(A):
    start = A
    while start is not None:
        print start.val,
        start = start.next
    print