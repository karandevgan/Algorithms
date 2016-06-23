class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double

    def findMedianOfFour(self, numA1, numA2, numB1, numB2):
        mid1 = max(numA1, numB1)
        mid2 = min(numA2, numB2)
        return (mid1 + mid2) / 2.0

    def findMedianOfThree(self, numA1, numB1, numB2):
        if numA1 >= numB1 and numA1 <= numB2:
            return numA1
        elif numA1 < numB1:
            return numB1
        else:
            return numB2

    def findMedianOfTwo(self, numA, numB):
        return (numA + numB) / 2.0

    def findMedianOfOneArray(self, Arr):
        if len(Arr) % 2 == 0:
            return (Arr[len(Arr) / 2] + Arr[len(Arr) / 2 - 1]) / 2.0
        else:
            return Arr[len(Arr) / 2]

    def findMedianSortedArrays(self, A, B):
        # import pdb
        # pdb.set_trace()
        if len(A) == 0:
            return self.findMedianOfOneArray(B)
        if len(B) == 0:
            return self.findMedianOfOneArray(A)

        # Assume that len(A) <= len(B)
        # Swap the arrays if len(A) > len(B)
        if len(A) > len(B):
            A, B = B, A

        if len(A) == 1:
            if len(B) % 2 == 0:
                return self.findMedianOfThree(A[0], B[len(B) / 2 - 1], B[len(B) / 2])
            elif len(B) > 2:
                medB = B[len(B) / 2]
                if A[0] >= B[len(B) / 2 - 1] and A[0] <= B[len(B) / 2 + 1]:
                    return self.findMedianOfTwo(A[0], medB)
                elif A[0] < medB:
                    return self.findMedianOfTwo(B[len(B) / 2 - 1], medB)
                else:
                    return self.findMedianOfTwo(medB, B[len(B) / 2 + 1])
            else:
                return self.findMedianOfTwo(A[0], B[0])

        if len(A) == 2 and len(B) % 2 == 0:
            if A[0] >= B[len(B) / 2 - 1] and A[1] <= B[len(B) / 2]:
                return self.findMedianOfTwo(A[0], A[1])
            elif A[0] < B[len(B) / 2 - 1] and A[1] > B[len(B) / 2]:
                return self.findMedianOfTwo(B[len(B) / 2 - 1], B[len(B) / 2])

        medA = self.findMedianOfOneArray(A)
        medB = self.findMedianOfOneArray(B)
        if medA == medB:
            return medA

        maxDiscardable = len(A) / 2 - 1
        if (len(A) % 2 != 0 or len(A) == 2):
            maxDiscardable = len(A) / 2
        if medA < medB:
            return self.findMedianSortedArrays(A[maxDiscardable:], B[:len(B) - maxDiscardable])
        else:
            return self.findMedianSortedArrays(A[:len(A) - maxDiscardable], B[maxDiscardable:])

A = [19,43]
B = [0, 4, 6, 18, 39, 42]

sol = Solution()
print sol.findMedianSortedArrays(A, B)
