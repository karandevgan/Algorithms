class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        A = A.strip()
        B = B.strip()

        i = 0
        while(A[i] == '0' and i != len(A)-1):
            i = i+1
        if i != 0:
            A = A[i:]

        i = 0
        while(B[i] == '0' and i != len(B)-1):
            i = i+1
        if i != 0:
            B = B[i:]

        if len(A) == 1 or len(B) == 1:
            if A == '1':
                return B
            elif B == '1':
                return A
            elif A == '0' or B == '0':
                return 0

        if len(A) < len(B):
            A,B = B,A

        intermediate = []
        k = len(B)-1
        for i in xrange(len(B)-1, -1, -1):
            carry = 0
            int_result = '0' * (len(B)-i-1)
            for j in xrange(len(A)-1, -1, -1):
                mul = str(int(B[i]) * int(A[j]) + carry)
                if len(mul) > 1:
                    carry = int(mul[0])
                    int_result += mul[1]
                else:
                    int_result += mul[0]
                    carry = 0
            if carry != 0:
                int_result += str(carry)
            intermediate.append(int_result)
            k -= 1
        carry = 0

        result = ''
        for i in xrange(len(intermediate[-1])):
            int_sum = 0
            for num in intermediate:
                if i >= len(num):
                    int_sum += 0
                else:
                    int_sum += int(num[i])
            int_sum += carry
            int_sum = str(int_sum)
            if len(int_sum) > 1:
                carry = int(int_sum[:len(int_sum)-1])
                int_sum = int_sum[len(int_sum)-1]
            else:
                carry = 0
            result += int_sum
        if carry != 0:
            result += str(carry)
        result = result[::-1]
        return result

sol = Solution()
print sol.multiply('3146777029336462037925782652721297369995237049791072180578322180785454700291', '36065384844986056037003129264314496654928054447')
