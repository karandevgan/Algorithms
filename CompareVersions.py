class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        isSwapped = False
        if len(A) > len(B):
            A,B = B,A
            isSwapped = True

        versionsA = [int(i) for i in A.split('.')]
        versionsB = [int(i) for i in B.split('.')]

        i = 0
        while i != len(versionsA):
            if versionsA[i] > versionsB[i]:
                if not isSwapped:
                    return 1
                else:
                    return -1
            elif versionsA[i] < versionsB[i]:
                if not isSwapped:
                    return -1
                else:
                    return 1
            i = i+1

        if i != len(versionsB):
            if sum(versionsB[i:]) > 0:
                if not isSwapped:
                    return -1
                else:
                    return 1
        return 0

sol = Solution()
print sol.compareVersion("13.0", "13.0.8")
