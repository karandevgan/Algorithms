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

    def findMedianOfOneArray(self, Arr, start, end):
        # import pdb
        # pdb.set_trace()
        lenArr = end - start + 1
        if lenArr % 2 == 0:
            return (Arr[start + lenArr / 2] + Arr[start + lenArr / 2 - 1]) / 2.0
        else:
            return Arr[start + lenArr / 2]

    def findMedianSortedArrays(self, A, B):
        # import pdb
        # pdb.set_trace()
        if len(A) == 0:
            return self.findMedianOfOneArray(B, 0, len(B)-1)
        if len(B) == 0:
            return self.findMedianOfOneArray(A, 0, len(A)-1)

        # Assume that len(A) <= len(B)
        # Swap the arrays if len(A) > len(B)
        if len(A) > len(B):
            A, B = B, A

        startA = 0
        endA = len(A) - 1
        startB = 0
        endB = len(B) - 1
        while True:
            lenA = endA - startA + 1
            lenB = endB - startB + 1

            if lenA == 1:
                if lenB % 2 == 0:
                    return self.findMedianOfThree(A[startA], B[startB + lenB / 2 - 1], B[startB + lenB / 2])
                elif lenB > 2:
                    medB = B[startB + lenB / 2]
                    if A[startA] >= B[startB + lenB / 2 - 1] and A[startA] <= B[startB + lenB / 2 + 1]:
                        return self.findMedianOfTwo(A[startA], medB)
                    elif A[startA] < medB:
                        return self.findMedianOfTwo(B[startB + lenB / 2 - 1], medB)
                    else:
                        return self.findMedianOfTwo(medB, B[startB + lenB / 2 + 1])
                else:
                    return self.findMedianOfTwo(A[startA], B[startB])

            if lenA == 2 and lenB % 2 == 0:
                if A[startA] >= B[startB + lenB / 2 - 1] and A[endA] <= B[startB + lenB / 2]:
                    return self.findMedianOfTwo(A[startA], A[endA])
                elif A[startA] < B[startB + lenB / 2 - 1] and A[endA] > B[startB + lenB / 2]:
                    return self.findMedianOfTwo(B[startB + lenB / 2 - 1], B[startB + lenB / 2])

            medA = self.findMedianOfOneArray(A, startA, endA)
            medB = self.findMedianOfOneArray(B, startB, endB)
            if medA == medB:
                return medA

            maxDiscardable = lenA / 2 - 1
            if (lenA % 2 != 0 or lenA == 2):
                maxDiscardable = lenA / 2
            if medA < medB:
                startA = startA + maxDiscardable
                endB = endB - maxDiscardable
                # return self.findMedianSortedArrays(A[startA + maxDiscardable:endA + 1], B[startB:endB - maxDiscardable + 1])
            else:
                endA = endA - maxDiscardable
                startB = startB + maxDiscardable

A = [ -40, -25, 5, 10, 14, 28, 29, 48 ]
B = [ -48, -31, -15, -6, 1, 8 ]

sol = Solution()
print sol.findMedianSortedArrays(A, B)
