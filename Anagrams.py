class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        anagrams_dict = {}
        for index, item in enumerate(A):
            sorted_item = ''.join(sorted(item))
            anagrams_index_list = anagrams_dict.get(sorted_item, [])
            anagrams_index_list.append(index+1)
            anagrams_dict[sorted_item] = anagrams_index_list
        return_list = anagrams_dict.values()
        return_list.sort()
        return return_list
            

sol = Solution()
A = ('cat', 'dog', 'god', 'tca')
print sol.anagrams(A)