class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        left = 0
        right = 0
        noOfZerosInWindow = 0
        if A[right] == 0:
            noOfZerosInWindow = 1
        
        bestLeft = 0
        bestRight = 0
        
        while right < len(A):
            if noOfZerosInWindow <= B:
                right += 1
                if right < len(A) and A[right] == 0:
                    noOfZerosInWindow += 1
                    
            if noOfZerosInWindow > B:
                while left < len(A) and A[left] != 0:
                    left += 1
                left += 1
                noOfZerosInWindow -= 1
            
            if right < len(A):
                if right - left > bestRight - bestLeft:
                    bestLeft = left
                    bestRight = right
            elif len(A) - 1 - left > bestRight - bestLeft:
                bestLeft = left
                bestRight = len(A) - 1
        return range(bestLeft, bestRight+1)

A = [ 0, 1, 1, 1 ]
sol = Solution()
print sol.maxone(A, 0)