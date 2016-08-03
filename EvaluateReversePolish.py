class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        operators = ['+', '-', '*', '/']
        for char in A:
            if char not in operators:
                stack.append(int(char))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.operation(op2, op1, char))
        return stack.pop()
                
    def operation(self, operand1, operand2, operator):
        result = 0
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        else:
            result = operand1 / operand2
        return result

sol = Solution()
A = ["4","2","5","*","+","1","3","2","*","+","/"]

print sol.evalRPN(A)