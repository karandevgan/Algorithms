class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0

        if (n == 0):
            return 1

        ans = 1
        isPositive = True

        if n % 2 != 0 and x < 0:
            isPositive = False

        square = abs(x)

        while (n != 0):
            if n % 2 != 0:
                ans = ans*square
            square = (square*square)%d
            n = n/2
            if (ans > d):
                ans = ans % d
        if not isPositive:
            return (ans*x) % d
        return ans
sol = Solution()
#print sol.pow(-5,5,20)
#print sol.pow(71045970, 41535484, 64735492)
print sol.pow(2,10,3)
