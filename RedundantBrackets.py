class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        operators = ['+', '*', '-', '/']
        stack = []
        for char in A:
            if char == '(':
                stack.append(char)
            elif char in operators:
                if len(stack) > 0:
                    stack.pop()

        if len(stack) > 0:
            return 1
        return 0

sol = Solution()
A = "(a + (a + b))"
#A = "( ( (a+b) * c ) * c / (a-d) ) + ( a+b * c/d )"
print sol.braces(A)