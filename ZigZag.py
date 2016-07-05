class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        # import pdb;
        # pdb.set_trace();
        final_list = []
        for i in xrange(B):
            final_list.append([])
        dir = 0
        index = 0
        for i in xrange(len(A)):
            if dir == 0:
                final_list[index].append(A[i])
                if index == B-1:
                    dir = 1
                else:
                    index += 1
            else:
                final_list[index - 1].append(A[i])
                index -= 1
                if index == 0:
                    dir = 0
                    index = 1

        return ''.join([''.join(i) for i in final_list])


sol  = Solution()
A = "ABCD"
B = 1
print sol.convert(A,B)