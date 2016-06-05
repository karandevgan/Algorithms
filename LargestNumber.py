def compare(number, number_to_insert):
    str_number_to_insert = str(number_to_insert)
    str_number = str(number)
    num1 = str_number + str_number_to_insert
    num2 = str_number_to_insert + str_number

    if num1 > num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

def largestNumber(A):
    '''
        Given a list of numbers, return the string arranging the numbers in
        the given list forming largest number. Eg: A = [3,30,90,9], the function
        should return 990330
    '''
    isAllZero = True
    for num in A:
        if num != 0:
            isAllZero = False

    if (isAllZero):
        return '0'

    A.sort(cmp=compare)
    return ''.join([str(i) for i in A])

A = [3, 30, 34, 5, 9]
print largestNumber(A)
