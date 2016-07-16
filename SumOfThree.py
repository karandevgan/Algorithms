class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        sum_of_three = 0
        temp_sum = 0
        diff = float('inf')
        temp_diff = 0

        for i in xrange(len(A)-2):
            j = i + 1
            k = len(A) - 1
            while j < k:
                temp_sum = A[i] + A[j] + A[k]
               
                if temp_sum == B:
                    return temp_sum
                
                temp_diff = max(B, temp_sum) - min(B, temp_sum)
               
                if temp_diff < diff:
                    diff = temp_diff
                    sum_of_three = temp_sum

                if temp_sum < B:
                    j += 1
                else:
                    k -= 1

        return sum_of_three

sol = Solution()
A = [ 5, -2, -1, -10, 10]

B = 5
print sol.threeSumClosest(A, B)