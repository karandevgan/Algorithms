class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        maxArea = 0 
        width = None
        i = 0

        while i < len(A):
            if (not len(stack) or A[stack[-1]] <= A[i]):
                stack.append(i)
                i += 1
            else:
                temp_pointer = stack.pop()
                width = i
                if len(stack):
                    width = i - stack[-1] - 1
                area = A[temp_pointer] * width

                maxArea = max(area, maxArea)

        while (len(stack)):
            temp_pointer = stack.pop() 
            
            width = i
            
            if len(stack):
                width = i - stack[-1] - 1

            area = A[temp_pointer] * width

            maxArea = max(area, maxArea)
        
        return maxArea
A = [2,1,5,6,2,3]

#A = [6, 2, 5, 4, 5, 1, 6]
sol = Solution()
print sol.largestRectangleArea(A)