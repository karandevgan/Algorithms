class Solution:
    # @param A : integer
    # @return a strings

    def intToRoman(self, A):
        # Reference Dict
        # romans = {
        #     1: 'I',
        #     5: 'V',
        #     10: 'X',
        #     50: 'L',
        #     100: 'C',
        #     500: 'D',
        #     1000: 'M'
        # }

        multiplier = 1
        result = []
        while (A != 0):
            digit = A % 10 * multiplier
            if multiplier == 1:
                if digit < 5:
                    if digit == 4:
                        result.append('IV')
                    else:
                        result.append('I' * digit)
                elif digit == 9:
                    result.append('IX')
                else:
                    result.append(('V' + 'I' * (digit - 5)))
            elif multiplier == 10:
                if digit < 50:
                    if digit == 40:
                        result.append('XL')
                    else:
                        result.append('X' * (digit / 10))
                elif digit == 90:
                    result.append('XC')
                else:
                    result.append(('L' + 'X' * ((digit - 50) / 10)))
            elif multiplier == 100:
                if digit < 500:
                    if digit == 400:
                        result.append('CD')
                    else:
                        result.append('C' * (digit / 100))
                elif digit == 900:
                    result.append('CM')
                else:
                    result.append(('D' + 'C' * ((digit - 500) / 100)))
            else:
                result.append('M' * (digit / 1000))
            A = A / 10
            multiplier *= 10
        result.reverse()
        return ''.join(result)


sol = Solution()
print sol.intToRoman(80)
