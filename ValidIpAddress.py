class Solution:
    # @param A : string
    # @return a list of strings

    def restoreIpAddresses(self, A):
        if len(A) > 12 and len(A) < 4:
            return []

        #import pdb; pdb.set_trace()
        valid_ips = []
        for i in xrange(3):
            part1 = A[:i + 1]
            if part1[0] == '0' and len(part1) > 1:
                continue
            if int(part1) > 255:
                continue
            remaining_1 = len(A) - len(part1)
            if remaining_1 > 9 or remaining_1 < 3:
                continue

            for j in xrange(i + 1, i + 4):
                part2 = A[i + 1:j + 1]
                if part2[0] == '0' and len(part2) > 1:
                    continue
                if int(part2) > 255:
                    continue
                remaining_2 = remaining_1 - len(part2)
                if remaining_2 > 6 or remaining_2 < 2:
                    continue

                for k in xrange(j + 1, j + 4):
                    part3 = A[j + 1:k + 1]
                    if part3[0] == '0' and len(part3) > 1:
                        continue
                    if int(part3) > 255:
                        continue
                    remaining_3 = remaining_2 - len(part3)
                    if remaining_3 > 3 or remaining_3 < 1:
                        continue

                    part4 = A[k + 1:]
                    if part4[0] == '0' and len(part4) > 1:
                        continue
                    if int(part4) > 255:
                        continue
                    valid_ips.append((part1, part2, part3, part4))
        valid_ips_strings = []
        for valid_ip in valid_ips:
            valid_ips_strings.append('.'.join(valid_ip))
        return valid_ips_strings

sol = Solution()
A = '0100100'
print sol.restoreIpAddresses(A)
