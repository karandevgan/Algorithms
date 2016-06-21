import pdb

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def isPossible(self, A, max_pages, num_of_students):
        total = 0
        count = 1

        for pages in A:
            total += pages
            if total > max_pages:
                count += 1
                total = pages
        return count

    def books(self, A, B):
        if B == 1:
            return sum(A)

        if B > len(A):
            return -1

        low = 0
        high = 0
        for pages in A:
            low = max(low, pages)
            high += pages
        while (low < high):
            mid = low + (high - low) / 2
            num_of_students = self.isPossible(A, mid, B)
            if num_of_students <= B:
                high = mid
            else:
                low = mid+1
        return low


# A = [12,34,67,90,110]
# A = [10, 11, 14, 17, 18, 22, 23, 25, 27, 29]
A = [91, 20, 62, 33, 97, 31, 88, 89, 73, 77, 4, 58, 0, 54, 60, 15, 47, 80, 30, 55, 46, 7, 38, 0, 26, 35, 57, 13]
#A = [ 53, 77, 8, 28, 33, 98, 81, 35, 13, 65, 14, 63, 36, 25, 69 ]

B = 24
sol = Solution()
print sol.books(A, B)
