import collections

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A) == 1:
            return 1
        if len(A) == 2:
            if A[0] <= A[1]:
                return 1
            else:
                return 2
        sorted_A = sorted(A)
        dict_letters = collections.OrderedDict()
        for char in sorted_A:
            if dict_letters.get(char) == None:
                dict_letters[char] = 1
            else:
                dict_letters[char] += 1
        rank = 0
        for i in xrange(len(A)-2):
            for key in dict_letters.keys():
                if key < A[i]:
                    if dict_letters.get(key) != 0:
                        numerator = len(A) - 1 - i
                        denominators = []
                        for key2 in dict_letters.keys():
                            if key == key2:
                                denominators.append(dict_letters.get(key2) - 1)
                            else:
                                denominators.append(dict_letters.get(key2))
                        upper_permutation, lower_permutation = self.permutation(numerator, denominators)
                        rank += (upper_permutation / lower_permutation)
                else:
                    break
            dict_letters[A[i]] -= 1
        if A[len(A)-2] <= A[len(A)-1]:
            rank += 1
        else:
            rank += 2
        return rank % 1000003


    def permutation(self, numerator, denominators):
        denominators.sort()
        max_denom = denominators[len(denominators)-1]
        upper_permutation = 1
        if max_denom != numerator:
            for j in xrange(max_denom+1, numerator+1):
                upper_permutation *= j
        lower_permutation = 1
        for j in xrange(len(denominators)-1):
            lower_permutation *= self.factorial(denominators[j])
        return upper_permutation, lower_permutation

    def factorial(self, A):
        if A == 1 or A == 0:
            return 1
        result = 1
        for i in xrange(2, A+1):
            result *= i
        return result

sol = Solution()
print sol.findRank('mmmmmmmmmmaaaaaaaa')
