class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def search(self, A, B):
        if len(A) == 1:
            if A[0] == B:
                return 0
            else:
                return -1
        if A[0] < A[len(A) - 1]:
            result = self.binarySearch(A, B, 0, len(A) - 1)
        else:
            rotated_index = self.binaryRotatedSearch(A)
            if A[rotated_index] == B:
                return rotated_index
            if rotated_index != 0 and A[rotated_index - 1] >= B and A[0] <= B:
                result = self.binarySearch(A, B, 0, rotated_index - 1)
            else:
                result = self.binarySearch(A, B, rotated_index + 1, len(A) - 1)
        return result

    def binarySearch(self, A, B, low, high):
        while (low <= high):
            mid = low + (high - low) / 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def binaryRotatedSearch(self, A):
        low = 0
        high = len(A) - 1
        while (low <= high):
            mid = low + (high - low) / 2
            prev = (mid - 1 + len(A)) % len(A)
            next = (mid + 1) % len(A)
            if A[mid] <= A[prev] and A[mid] <= A[next]:
                return mid
            elif A[mid] < A[high]:
                high = mid - 1
            else:
                low = mid + 1

sol = Solution()
#A = (2,3)
A = (180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85,
     87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177)
print sol.search(A, 42)
