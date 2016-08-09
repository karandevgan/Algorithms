class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        pallindromes_dict = {}
        pallindromes_dict[A[-1]] = [[A[-1]]]

        for i in xrange(len(A)-2, -1, -1):
            dict_list = []
            
            for j in xrange(i, len(A)):
                
                if self.isPallindrome(A[i:j+1]):
                    if j < len(A)-1:
                        
                        for pallindromes in pallindromes_dict.get(A[j+1:]):
                            temp_list_of_pallindromes=[A[i:j+1]]
                            for pallindrome in pallindromes:
                                temp_list_of_pallindromes.append(pallindrome)
                            dict_list.append(temp_list_of_pallindromes)
                    
                    else:
                        dict_list.append([A[i:j+1]])       
            
            pallindromes_dict[A[i:]] = dict_list
        
        return pallindromes_dict.get(A)

    def isPallindrome(self, A):
        return A == A[::-1]

sol = Solution()
print sol.partition("efe")