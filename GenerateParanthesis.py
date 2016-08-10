class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        self.paranthesis_list = []
        self.paranthesis_list.append('(')
        self.addBracket(A)
        self.paranthesis_list.sort()
        return self.paranthesis_list

    def addBracket(self, A):
        isListChanged = False
        n = len(self.paranthesis_list)
        for i in xrange(n):
            item = self.paranthesis_list[i]
            if len(item) == 2*A:
                continue
            no_of_close_brackets, no_of_open_brackets = self.countBrackets(item)
            isItemChanged = False
            
            if no_of_close_brackets + 1 <= no_of_open_brackets:
                self.paranthesis_list[i] = item + ')'
                isListChanged = True
                isItemChanged = True

            if no_of_open_brackets + 1 <= A:
                if not isItemChanged:
                    self.paranthesis_list[i] = item + '('
                else:
                    self.paranthesis_list.append(item + '(')
                isListChanged = True

        if isListChanged:
            self.addBracket(A)
        else:
            return
            
    
    def countBrackets(self, string_of_paranthesis):
        no_of_open_brackets = 0
        no_of_close_brackets = 0
        for char in string_of_paranthesis:
            if char == '(':
                no_of_open_brackets += 1
            elif char == ')':
                no_of_close_brackets += 1
        return (no_of_close_brackets, no_of_open_brackets)