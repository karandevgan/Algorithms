class Solution:
    def power(self, num, n):
        if n==0:
            return 1
        if n==1:
            return num

        #Recursive method
        # temp = self.power(num,n/2)
        # if (n % 2 != 0):
        #     return num * temp * temp
        # else:
        #     return temp * temp

        #Iterative method
        temp = num
        result = 1
        while (n != 0):
            if (n % 2 != 0):
                result *= num
            num = num * num
            n /= 2
        return result

sol = Solution()
print sol.power(54,12)
