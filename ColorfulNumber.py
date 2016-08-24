class Solution:
    '''
        Check if number is colorful.
        A number is colorful if product of all its subpart is different
    '''
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        # import pdb
        # pdb.set_trace()
        products = {}
        A = str(A)
        for i in xrange(len(A)):
            for j in xrange(i, len(A)):
                new_product = int(A[i])
                k = i+1
                while k <= j:
                    new_product *= int(A[k])
                    k += 1
                new_product = str(new_product)
                if products.get(new_product) is not None:
                    return 0
                products[new_product] = 1
        return 1

sol = Solution()
print sol.colorful(12)