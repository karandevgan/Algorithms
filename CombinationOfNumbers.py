class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        combine_list = []
        for i in xrange(1, n - k + 2):
            lists = self.auxillary(i, n, k)
            for sublist in lists:
                combine_list.append(sublist)
        return combine_list
    
    def auxillary(self, start_num, last_num, k):
        return_list = []
        if k == 1:
            return_list.append([start_num])
            return return_list
        k = k-1
        for i in xrange(start_num+1, last_num - k + 2):
            int_lists = self.auxillary(i, last_num, k)
            for sublist in int_lists:
                return_list.append([start_num] + sublist)
        return return_list

sol = Solution()
print sol.combine(5,2)