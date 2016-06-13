class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, integer):
        if self.top == -1:
            self.top = 0
        if self.top == len(self.stack):
            return False
        else:
            self.stack[self.top] = integer
            self.top += 1
            return True

    def pop(self):
        if self.top == -1:
            return None
        else:
            elem = self.stack[self.top-1]
            self.stack[self.top-1] = None
            self.top -= 1
            return elem

    def peek(self):
        if self.top == -1:
            return None
        else:
            return self.stack[self.top]

    def __repr__(self):
        return_str = ''
        if self.top == -1:
            return 'Empty Stack'
        index = 0
        while (index < self.top-1):
            return_str += str(self.stack[index]) + ", "
            index += 1
        return_str += str(self.stack[self.top-1])
        return return_str
