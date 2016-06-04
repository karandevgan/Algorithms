import random
import time
import pdb


def Partition(A, start, end, pivot_index):
    if pivot_index != end:
        A[end], A[pivot_index] = A[pivot_index], A[end]
    pivot = A[end]
    j = start
    for index in xrange(start, end):
        if A[index] <= pivot:
            if j != index:
                A[j], A[index] = A[index], A[j]
            j += 1
    A[j], A[end] = A[end], A[j]
    return j


def Select(A, smallest_index, start=0, end=None):
    # pdb.set_trace()
    group_size = 20
    if (end == None):
        end = len(A) - 1
    if (start == end):
        return A[start]
    if (len(A) <= group_size):
        A.sort()
        median_of_medians = A[len(A)/2]
    # else:
    #     groups = [A[i:i + group_size]
    #               for i in xrange(start, end + 1, group_size)]
    #     for group in groups:
    #         group.sort()
    #     medians = [group[len(group)/2] for group in groups]
    #     if len(medians) <= 10:
    #         medians.sort()
    #         median_of_medians = medians[len(medians)/2]
    #     else:
    #         median_of_medians = Select(medians, len(medians)/2, 0, len(medians)-1)
    #
    # L1 = filter(lambda x: x < median_of_medians, A)
    # k = len(L1) + 1
    # if k == smallest_index:
    #     return median_of_medians
    # elif k > smallest_index:
    #     return Select(L1, smallest_index)
    # else:
    #     L2 = filter(lambda x: x > median_of_medians, A)
    #     return Select(L2, smallest_index - k)

    else:
        j = start
        group_end_index = 0
        median_index = 0
        for i in xrange(start, end+1, group_size):
            group_end_index = i + (group_size-1)
            if group_end_index > end:
                group_end_index = end
            A[i:group_end_index+1] = sorted(A[i:group_end_index+1])
            median_index = (group_end_index+i)/2
            A[median_index], A[j] = A[j], A[median_index]
            j += 1
        j-=1
        if (j-start+1) <= 5:
            A[start:j+1] = sorted(A[start:j+1])
            median_of_medians = A[(start+j)/2]
        else:
            median_of_medians = Select(A, (start+j)/2, start, j)
        pivot_index = Partition(A, start, end, (start+j)/2)
    k = pivot_index + 1
    if k == smallest_index:
        return A[pivot_index]
    elif k < smallest_index:
        return Select(A, smallest_index, pivot_index+1, end)
    else:
        return Select(A, smallest_index, start, pivot_index-1)


#A = [1,2,3,4,5,10,9,8,7,6,13,11,12]
t1 = 0.0
t2 = 0.0
list_size = 100000
for i in xrange(10):
    A = random.sample(xrange(10000000000), list_size)
    start_time = time.time()
    Select(A, 8)
    t1 += time.time() - start_time
    A = random.sample(xrange(10000000000), list_size)
    start_time = time.time()
    sorted(A)
    t2 += time.time() - start_time


print t1/10
print t2/10
