class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        #import pdb; pdb.set_trace()
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        elif len(haystack) < len(needle):
            return -1
        elif len(needle) == 0:
            return -1

        i = 0
        j = 0
        start_index = -1
        another_index = -1

        while i < len(haystack) and j < len(needle):
            remaining_haystack = len(haystack) - i - 1
            remaining_needle = len(needle) - j - 1

            if remaining_needle > remaining_haystack:
                return -1

            if haystack[i] == needle[0] and another_index <= start_index:
                another_index = i

            if haystack[i] == needle[j]:
                if j == 0:
                    start_index = i
                i += 1
                j += 1
            else:
                j = 0
                # start_index != 1 checks for the case when first character is
                # also not matched atleast for once
                if another_index > start_index and start_index != -1:
                    i = another_index
                else:
                    i += 1
                # Start index should become -1 after every non match character
                start_index = -1
        if j != len(needle):
            start_index = -1

        return start_index


sol = Solution()
haystack = "babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba"
needle = "bababbbbbbabbbaabbaaabbbaababa"
print sol.strStr(haystack, needle)
