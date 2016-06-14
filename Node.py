class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.key)

if __name__ == '__main__':
    # Code for the main function
    # from copy import copy
    # n1 = Node(45)
    # n2 = copy(n1)
    # n1.key = 56
    # print n2
    pass
