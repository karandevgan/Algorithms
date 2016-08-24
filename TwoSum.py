class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {}
        for index, value in enumerate(A):
            l = d.get(value, [])
            if len(l) < 2:
                l.append(index)
                d[value] = l
        
        result = []

        index1 = -1
        index2 = -1
        rem = 0
        rem_index_list = []
        dict_items = d.items()
        
        for item in dict_items:
            rem = B - item[0]
            if rem == item[0] and len(item[1]) > 1:
                index1 = item[1][0]
                index2 = item[1][1]
            elif rem != item[0]:
                rem_index_list = d.get(rem, [])
                if len(rem_index_list) != 0:
                    index1 = min(item[1][0], rem_index_list[0])
                    index2 = max(item[1][0], rem_index_list[0])
                
            if index1 != None and index2 != None and (len(result) == 0 or result[1] > index2):
                result = []
                result.append(index1)
                result.append(index2)
        
        if len(result) > 1:
            result[0] += 1
            result[1] += 1
        return result

sol  = Solution()
A = [1,1,1,1]

print sol.twoSum(A,2)