
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getRequiredPainters(self, C, max_length):
        size = len(C)
        count = 1
        total = 0
        for i in xrange(size):
            total += C[i]
            if total > max_length:
                count += 1
                total = C[i]
        return count

    def partition(self, A, C):
        num_of_painters = A
        low = max(C)
        high = sum(C)
        while (low < high):
            mid = low + (high - low) / 2
            required_painters = self.getRequiredPainters(C, mid)
            if required_painters <= num_of_painters:
                high = mid
            else:
                low = mid + 1

        return low

    def paint(self, A, B, C):
        partition = self.partition(A, C)
        return int ((partition * B) % 10000003)

sol = Solution()
A = 3
B = 5
C = [i for i in xrange(1,11)]
print sol.paint(A,B,C)
