class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A==0:
            return ''
        if A==1:
            return '1'
        if A==2:
            return '11'
        s = ['1', '1']
        # for i in xrange(3, A+1):

        for i in xrange(3, A+1):
            prevChar = s[0]
            count_of_char = 1
            newString = []
            for j in xrange(1,len(s)):
                if s[j] == prevChar:
                    count_of_char += 1
                else:
                    newString.append(str(count_of_char))
                    newString.append(prevChar)
                    prevChar = s[j]
                    count_of_char = 1
            newString.append(str(count_of_char))
            newString.append(s[j])
            s = newString

        return ''.join(newString)

sol = Solution()
print sol.countAndSay(29)
