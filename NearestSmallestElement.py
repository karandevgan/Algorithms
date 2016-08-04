class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        return_arr = []
        stack = [arr[0]]
        return_arr.append(-1)
        for i in xrange(1,len(arr)):
            isSmallerElementFound = False
            while len(stack) > 0:
                if stack[-1] < arr[i]:
                    isSmallerElementFound = True
                    return_arr.append(stack[-1])
                    break
                else:
                    stack.pop()
            stack.append(arr[i])
            if not isSmallerElementFound:
                return_arr.append(-1)
        return return_arr

A = [1,4,5,2,10,7,3,8]
sol = Solution()
print sol.prevSmaller(A)