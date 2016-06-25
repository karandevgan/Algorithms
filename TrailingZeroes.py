class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        divisor = 5
        zeroes = 0
        while (A != 0):
            zeroes += A / divisor
            A = A / divisor
        return zeroes



import unittest
class TrailingZeroesTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_4(self):
        actual = self.sol.trailingZeroes(4)
        expected = 0
        fail_message = 'Expected: %s, Actual: %s' % (expected, actual)
        self.assertEqual(expected, actual, fail_message)

    def test_5(self):
        actual = self.sol.trailingZeroes(5)
        expected = 1
        fail_message = 'Expected: %s, Actual: %s' % (expected, actual)
        self.assertEqual(expected, actual, fail_message)

    def test_10(self):
        actual = self.sol.trailingZeroes(10)
        expected = 2
        fail_message = 'Expected: %s, Actual: %s' % (expected, actual)
        self.assertEqual(expected, actual, fail_message)



if __name__ == '__main__':
    unittest.main()
