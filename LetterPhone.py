from collections import deque

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        combination = {
            "1": "1",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "0"
            }
        
        temp_list = deque()
        number_of_digits = len(A)
        for char in combination.get(A[0]):
            temp_list.append(char)

        return self.appendToList(1, len(A)-1, combination, A, temp_list)

    def appendToList(self, curr_depth, max_depth, combination, A, temp_list):
        if max_depth == 0:
            return temp_list
            
        original_length = len(temp_list)
        for i in xrange(original_length):
            string = temp_list.popleft()
            for char in combination.get(A[curr_depth]):
                temp_list.append(string + char)
        

        if curr_depth != max_depth:
            return self.appendToList(curr_depth+1, max_depth, combination, A, temp_list)
        else:
            return temp_list

sol = Solution()
print sol.letterCombinations("2")