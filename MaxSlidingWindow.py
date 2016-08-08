from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if len(A) <= 1:
            return A
        return_arr = []
        d = deque()
        i = 0
        
        while i < len(A) and i < B:
            while len(d) != 0 and A[i] > d[-1]:
                d.pop()
            d.append(A[i])
            i += 1
        return_arr.append(d[0])

        while i < len(A):
            if len(d) != 0 and d[0] == A[i-B]:
                d.popleft()
            while len(d) != 0 and A[i] > d[-1]:
                d.pop()
            d.append(A[i])
            return_arr.append(d[0])
            i += 1
        return return_arr
A = [1,3,-1,-3,5,3,6,7]
#A = [ 648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308, 440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482, 558, 937, 207, 368 ]
B = 3
sol = Solution()
print sol.slidingMaximum(A,B)        