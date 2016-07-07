class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A == 0:
            return 0
        #bits = [0 for _ in xrange(32)]
        index = 31
        number = 0
        while (A != 0):
            #bits[index] = A % 2
            if A % 2 == 1:
                number += 2**index
            A = A/2
            index -= 1
        return number

sol = Solution()
print sol.reverse(1)