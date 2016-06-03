import random

def SimultaneousMinMax(A):
    '''
        Finds the maximum and minimum numbers from the list using two algos:
        1. Comparing each element with min and max
        2. Comparing pairs and then with min and max
        We found that for list of n integers, first method took n-1 comparisons
        each for min and max but the second method took atmost of 3 * floor(n/2)
        comparisons.
    '''
    if len(A) == 0:
        return None

    if len(A) == 1:
        return (A[0],A[1])

    number_of_comparisons = 0
    min_element = A[0]
    max_element = A[0]
    for i in xrange(1, len(A)):
        if (A[i] < min_element):
            min_element = A[i]
        if (A[i] > max_element):
            max_element = A[i]
        number_of_comparisons += 2

    print "Number of Comparisons with naive algo: ", number_of_comparisons
    print (min_element, max_element)

    number_of_comparisons = 0

    if (len(A) % 2 != 0):
        min_element = A[0]
        max_element = A[0]
        start_index = 1
    else:
        if (A[0] > A[1]):
            max_element = A[0]
            min_element = A[1]
        else:
            max_element = A[1]
            min_element = A[0]
        start_index = 2

    number_of_comparisons += 1

    for i in xrange(start_index, len(A), 2):
        if (A[i] < A[i+1]):
            if (A[i] < min_element):
                min_element = A[i]
            if (A[i+1] > max_element):
                max_element = A[i+1]
        else:
            if (A[i+1] < min_element):
                min_element = A[i+1]
            if (A[i] > max_element):
                max_element = A[i]
        number_of_comparisons += 3

    print "Number of comparisons by comparing in pair: ", number_of_comparisons
    return (min_element, max_element)

if __name__=="__main__":
    A = [random.randint(1,1000) for _ in xrange(2000)]
    #A = [1,5,2,3,7,8,10]
    print SimultaneousMinMax(A)
