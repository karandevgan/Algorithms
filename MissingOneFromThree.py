'''
    Given a list of integers, every integer appears thrice except one.
    Return that one integer.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer

    def singleNumber(self, A):
        # ones store bits which appear only once
        ones = 0
        # twos store bits which appear twice
        twos = 0
        # bits is in ones and twos also.
        common = 0
        for num in A:
            # If bits appears first time, ones & num return 0 and bits are not recorded in twos.
            twos = twos | (ones & num)
            # If bits appears first time, ones records the bits. If its the second time then the bits are removed from the ones.
            ones = ones ^ num
            # Bits appear third time, so its recorded in ones and twos both
            # Make the common bits between ones and twos to 0
            common = ~(ones & twos)
            # Removes the common bits From ones and twos
            ones &= common
            twos &= common
        return ones

sol = Solution()
A = [1,4,5,1,1,4,4]
print sol.singleNumber(A)