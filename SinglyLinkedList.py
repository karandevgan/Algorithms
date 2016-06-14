from Node import Node

class SingleLinkedList:
    def __init__(self):
        self.HEAD = Node()
        self.TAIL = Node()
        self.HEAD.next = self.TAIL
        self.length = 0

    def insert(self, key, pos=0):
        if pos < 0 or pos > self.length:
            raise ValueError

        new_node = Node(key)

        if pos == 0:
            new_node.next = self.HEAD.next
            self.HEAD.next = new_node
        else:
            curr_node = self.HEAD.next
            prev_node = self.HEAD
            for i in xrange(pos):
                prev_node = curr_node
                curr_node = curr_node.next
            new_node.next = curr_node
            prev_node.next = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index > self.length:
            raise ValueError
        curr_node = self.HEAD
        for i in xrange(index+1):
            curr_node = curr_node.next
        return curr_node

    def search(self, key):
        curr_node = self.HEAD.next
        key_index = -1
        index = -1
        while (curr_node.key != None):
            index += 1
            if curr_node.key == key:
                key_index = index
                break
            curr_node = curr_node.next
        return key_index

    def delete(self, key):
        prev_node = self.HEAD
        curr_node = self.HEAD.next
        key_index = -1
        index = -1
        while (curr_node.key != None):
            index += 1
            if curr_node.key == key:
                prev_node.next = curr_node.next
                del curr_node
                key_index = index
                break
            prev_node = curr_node
            curr_node = curr_node.next
        return key_index

    def reverse(self, index = 0):
        if index == 0:
            start_node = self.HEAD
        else:
            start_node = self.get(index-1)
        curr_node = start_node.next
        new_next = self.TAIL
        prev_node = None
        while (curr_node.key != None):
            temp = curr_node.next
            curr_node.next = new_next
            new_next = curr_node
            curr_node = temp
        start_node.next = new_next

    def __repr__(self):
        curr_node = self.HEAD.next
        return_str = ''
        while (curr_node.key != None):
            return_str += str(curr_node) + ' '

            curr_node = curr_node.next
        if return_str == '':
            return 'None'
        return return_str

if __name__ == '__main__':
    ll = SingleLinkedList()

    for i in xrange(10):
        ll.insert(i)

    print ll
    ll.reverse(9)
    print ll
    #
    # print ll.delete(6)
    # print ll
    #
    # print ll.get(8)
