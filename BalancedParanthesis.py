class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        open_parenthesis = ['(', '{', '[']
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for x in A:
            if x in open_parenthesis:
                stack.append(x)
            else:
                if len(stack) > 0:
                    temp = stack.pop()
                    if pairs.get(x) != temp:
                        return 0
                else:
                    return 0
        if len(stack) > 0:
            return 0
        return 1

A = ")))"
sol = Solution()
print sol.isValid(A)