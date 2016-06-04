import random

def RandomizedPartition(A, p, r):
    pivot_index = random.randint(p, r)
    A[r], A[pivot_index] = A[pivot_index], A[r]
    pivot = A[r]
    j = p;
    for i in xrange(p,r):
        if A[i] <= pivot:
            if i != j:
                A[i], A[j] = A[j], A[i]
            j += 1
    A[r], A[j] = A[j], A[r]
    return j

def RandomizedSelection(A, p, r, i):
    '''
        Selects 'i'th smallest element from the list.
        This algorithm outperforms other if the elements in the list are
        distinct.
    '''
    if p == r:
        return A[p]
    q = RandomizedPartition(A, p, r)
    # k = q - p + 1
    k = q+1
    if k == i:
        return A[q]
    elif i < k:
        return RandomizedSelection(A, p, q-1, i)
    else:
        # return RandomizedSelection(A, q+1, r, i-k)
        return RandomizedSelection(A, q+1, r, i)

def GetElement(A, i):
    if i < 1 or i > len(A):
        return None
    else:
        return RandomizedSelection(A, 0, len(A)-1, i)

A = random.sample(xrange(-30,30), 10)
print A
print GetElement(A, 5)
