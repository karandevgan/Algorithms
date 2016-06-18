import bisect

def getPrimes(num):
    primes = [1] * (num+1)
    primes[0] = 0
    primes[1] = 0
    return_list = []
    for i in xrange(2, num+1):
        if primes[i] == 1:
            return_list.append(i)
            j = 2
            while (i * j <= num):
                primes[i*j] = 0
                j += 1
    return return_list

def isPrime(prime_numbers_upto_A, num):
    i = bisect.bisect_left(prime_numbers_upto_A, num)
    if i != len(prime_numbers_upto_A) and prime_numbers_upto_A[i] == num:
        return True
    return False

def primesum(A):
    prime_numbers_upto_A = getPrimes(A)
    for num in prime_numbers_upto_A:
        if A-num == num:
            return [num, A-num]
        if isPrime(prime_numbers_upto_A, A-num):
            return [num, A-num]

print primesum(10)
