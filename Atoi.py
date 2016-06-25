class Solution:
    # @param A : string
    # @return an integer

    def atoi(self, A):
        A = A.lstrip()
        if len(A) < 1:
            return 0

        INT_MAX = '2147483647'
        INT_MIN = '-2147483648'

        isNegative = False
        start_index = 0

        returnNumberString = ''
        if A[0] == '-':
            isNegative = True
            start_index = 1
            returnNumberString = '-'
        if A[0] == '+':
            start_index = 1
        integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in xrange(start_index, len(A)):
            if A[i] in integers:
                returnNumberString += A[i]
            else:
                break

        if returnNumberString == '' or returnNumberString == '-':
            return 0
        else:
            if (isNegative and len(returnNumberString) >= len(INT_MIN)):
                if len(returnNumberString) > len(INT_MIN) or \
                        returnNumberString > INT_MIN:
                    return int(INT_MIN)
            elif (not isNegative and len(returnNumberString) >= len(INT_MAX)):
                if len(returnNumberString) > len(INT_MAX) or \
                        returnNumberString > INT_MAX:
                    return int(INT_MAX)
            return int(returnNumberString)

sol = Solution()
print sol.atoi(' +7')
