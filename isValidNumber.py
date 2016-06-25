class Solution:
    # @param A : string
    # @return an integer

    def isNumber(self, A):
        A = A.strip()
        if len(A) == 0:
            return 0
        if len(A) == 1 and (A[0] == '-' or A[0] == '+'):
            return 0

        start_index = 0

        if A[0] == '-' or A[0] == '+':
            start_index += 1
        if start_index != 0:
            A = A[start_index:]

        # Split around the exponent (e)
        exponent_splits = A.split('e')

        # First part of exponent split should be the decimal number
        number = exponent_splits[0]

        # There is only two parts of split. One is mantissa and other is
        # exponent. If mantissa == '' or if total splits > 2, number is invalid
        if len(exponent_splits) > 3 or number == '':
            return 0

        power = ''
        if len(exponent_splits) > 1:
            power = exponent_splits[1]

        # Split around the decimal point
        number_splits = number.split('.')

        # There can be only one decimal point.
        # If there is no digit after the decimal point, number is invalid
        if len(number_splits) > 2 or number_splits[-1] == '':
            return 0

        for subnumber in number_splits:
            if subnumber == '':
                break
            for char in subnumber:
                if not char.isdigit():
                    return 0

        if power != '':
            power_start_index = 0
            if power[0] == '-' or power[0] == '+':
                power_start_index += 1
            if power_start_index != 0:
                power = power[power_start_index:]
            # According to problem, power should not contain decimal numbers
            if len(power.split('.')) > 1:
                return 0
            for char in power:
                if not char.isdigit():
                    return 0
        return 1
sol = Solution()
print sol.isNumber('2.')
