def get_nth_digit(num, n):
    '''
        This function returns the nth digit of a number num
        n = digit which is required
        num = number
    '''
    divisor = 10 ** n
    dividend = num
    new_dividend = dividend % divisor
    return new_dividend / (divisor / 10)

def counting_sort(A, n):
    count = [0] * 10
    aux_list = [0] * len(A)

    for num in A:
        count[get_nth_digit(num, n)] += 1

    for i in xrange(1,len(count)):
        count[i] += count[i-1]

    nth_digit = -1
    for i in xrange(len(A)-1, -1, -1):
        nth_digit = get_nth_digit(A[i], n)
        aux_list[count[nth_digit]-1] = A[i]
        count[nth_digit] -= 1

    return aux_list

def radix_sort(A):
    max_num = max(A)
    max_digits = 0
    while (max_num != 0):
        max_digits += 1
        max_num = max_num / 10
    for i in xrange(1, max_digits+1):
        B = counting_sort(A, i)
    return B

A = [329, 457, 657, 839, 436, 720, 355]
A = radix_sort(A)
print A
