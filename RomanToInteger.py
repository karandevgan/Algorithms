class Solution:
    def romanToInt(self, A):
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

        number = 0
        i = 0

        while (i < len(A)):
            num1 = romans.get(A[i])
            if i != len(A) - 1:
                num2 = romans.get(A[i+1])
            else:
                num2 = 0

            if num1 < num2:
                number += num2 - num1
                i += 2
            else:
                number += num1
                i += 1
        return number

sol = Solution()
print sol.romanToInt('CXXVI')
