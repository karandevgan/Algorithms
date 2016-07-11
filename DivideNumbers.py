class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
                
        
        isNegative = (dividend < 0 and divisor > 0)  or (dividend > 0 and divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend < divisor:
            return 0
        
        count = 0
        temp_divisor = divisor
        temp_count = 1

        while (dividend >= divisor):
            if dividend == divisor:
                count += 1
                break
            
            while (temp_divisor << 1 <= dividend):
                temp_divisor = temp_divisor << 1
                temp_count = temp_count << 1
            
            dividend -= temp_divisor
            temp_divisor = divisor
            count += temp_count
            temp_count = 1
        
        if isNegative:
            count = -count
        if count < MIN_INT or count > MAX_INT:
            count = MAX_INT
        return count

sol = Solution()
print sol.divide(-8,-2)