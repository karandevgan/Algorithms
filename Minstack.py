class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = []
        self.tempStack = []

    def push(self, x):
        self.stack.append(x)

        if len(self.tempStack) == 0 or self.tempStack[-1] > x:
            self.tempStack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            x = self.stack.pop()
            if self.tempStack[-1] == x:
                self.tempStack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        
        return -1

    # @return an integer
    def getMin(self):
        if len(self.tempStack) > 0:
            return self.tempStack[-1]
        
        return -1