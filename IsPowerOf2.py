class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if A == '1' or A == '0':
            return 0
        while (A != '1'):
            if int(A[len(A)-1]) % 2 == 0:
                A = self.divideBy2(A)
            else:
                return 0
        return 1

    def divideBy2(self, A):
        #import pdb; pdb.set_trace()
        result = []
        i = len(A) - 1
        current = A[i]
        isRemainder = False
        while (i != 0):
            if int(current) < 2:
                if result != [] and not isRemainder:
                    result.append('0')
                i = i + 1
                if i != len(A):
                    current += A[i]
            else:
                result.append(str(int(current) / 2))
                current = str(int(current) % 2)
                isRemainder = True
                if int(current) == 0:
                    isRemainder = False
                    i = i + 1
                    if i != len(A):
                        current = A[i]
        results = ''.join(result)
        return results
sol = Solution()
#print sol.divideBy2('1')
A = str(2 << 6000)

print sol.power(A)
