class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double

    def findMedianSortedArrays(self, A, B):
        if len(A) <= len(B):
            return self.findMedian(A, 0, len(A) - 1, B, 0, len(B) - 1)
        else:
            return self.findMedian(B, 0, len(B) - 1, A, 0, len(A) - 1)

    def findMedian(self, A, lowA, highA, B, lowB, highB):
        #import pdb; pdb.set_trace()
        m = highA - lowA + 1
        n = highB - lowB + 1
        # m and n are lengths of A and B
        # Assume m <= n
        # No elements in A
        if m == 0:
            if n % 2 == 0:
                return (B[lowB + n / 2] + B[lowB + n / 2 - 1]) / 2.0
            else:
                return B[lowB + n / 2]

        # Only One element in A
        if m == 1:
            if n == 1:
                return (A[lowA] + B[lowB]) / 2.0
            if n % 2 == 0:
                mid1 = B[lowB + n / 2 - 1]
                mid2 = B[lowB + n / 2]
                if A[lowA] > mid1 and A[lowA] < mid2:
                    return A[lowA]
                elif A[lowA] <= mid1:
                    return mid1
                else:
                    return mid2
            else:
                mid1 = B[lowB + n / 2]
                return (A[lowA] + mid1) / 2.0

        # Two elements in A
        if m == 2:
            if n % 2 == 0:
                mid1 = B[lowB + (n / 2 - 1)]
                mid2 = B[lowB + (n / 2)]
                if n == 2:
                    left = max(A[lowA], mid1)
                    right = min(A[highB], mid2)
                else:
                    left = max(A[lowA], B[lowB + (n / 2 - 2)])
                    right = min(A[highA], B[lowB + (n / 2) + 1])
                temp_list = sorted([left, right, mid1, mid2])
                return (temp_list[1] + temp_list[2]) / 2.0
            else:
                mid1 = B[lowB + n / 2]
                left = max(A[lowA], B[lowB + n / 2 - 1])
                right = min(A[highA], B[lowB + n / 2 + 1])
                temp_list = sorted([left, right, mid1])
                return temp_list[1]

        midA = (m-1) / 2
        midB = (n-1) / 2
        if A[midA] <= B[midB]:
            return self.findMedian(A, midA, highA, B, lowB, highB - midA - 1)
        else:
            return self.findMedian(A, lowA, midA, B, lowB + midA, highB)


A = [1]
B = [2,3,4,5,6]

sol = Solution()
print sol.findMedianSortedArrays(A, B)
