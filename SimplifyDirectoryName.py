class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A.strip('/')
        directories = []
        temp_list = A.split('/')
        for dir in temp_list:
            if dir == '.' or dir == '':
                continue
            elif dir == '..' and len(directories) > 0:
                directories.pop()
            elif dir != '..':
                directories.append(dir)
        s = '/' + '/'.join(directories)
        return s

A = "///home////b/"
sol = Solution()
print sol.simplifyPath(A)
