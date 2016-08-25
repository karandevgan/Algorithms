class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        d = {}
        
        start = 0
        end = -1

        sum = 0
        for i in xrange(0, len(A)):
            sum += A[i]
            
            if sum == 0:
                end = i
            else:
                indices_list = d.get(sum, [])
                if len(indices_list) == 2:
                    indices_list[1] = i
                else:
                    indices_list.append(i)
                d[sum] = indices_list
    

        if d.get(0) is not None:
            start = 0
            end = d.get(0)[-1]

        for key, value in d.items():
            if len(value) == 1:
                continue
            
            if end == -1:
                start = value[0] + 1
                end = value[-1]
            else:
                max_length = end-start
                curr_length = value[-1] - value[0] - 1
                if (max_length < curr_length) or \
                    (max_length == curr_length and value[0] + 1 < start):
                    start = value[0] + 1
                    end = value[-1]
                    
        return A[start:end+1]

sol = Solution()
A =  [1 ,2 ,12 ,-4 ,-4, 0 ]
print sol.lszero(A)