class Solution:
    # @param A : string
    # @param B : string
    # @return a strings

    def addBinary(self, A, B):
        if len(A) == 0:
            return B

        if len(B) == 0:
            return A

        if len(A) < len(B):
            A, B = B, A

        #import pdb; pdb.set_trace()
        difference_between_lengths = len(A) - len(B)

        result = ''
        carry = 0
        i = len(B) - 1
        j = len(A) - 1
        while i != -1:
            carry_sum = carry + int(A[j])
            if carry_sum == 2:
                carry = 1
                carry_sum = 0
            else:
                carry = 0

            final_sum = carry_sum + int(B[i])

            if final_sum == 2:
                result += '0'
                carry = 1
            else:
                result += str(final_sum)
            i -= 1
            j -= 1

        while j != -1:
            carry_sum = carry + int(A[j])
            if carry_sum == 2:
                result += '0'
                carry = 1
            else:
                result += str(carry_sum)
                carry = 0
            j -= 1

        if carry != 0:
            result += '1'
        return result[::-1]

sol = Solution()
print sol.addBinary('1010110111001101101000', '1000011011000000111100110')
