import random
import time
import pdb
from InsertionSort import InsertionSort

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
    group_size = 5
    if (end == None):
        end = len(A) - 1
    if (start == end):
        return A[start]
    if (len(A) <= group_size):
        A.sort()
        median_of_medians = A[len(A)/2]
    else:
        j = start
        group_end_index = 0
        median_index = 0
        for i in xrange(start, end+1, group_size):
            group_end_index = i + (group_size-1)
            if group_end_index > end:
                group_end_index = end
            A[i:group_end_index+1] = sorted(A[i:group_end_index+1])
            #A = InsertionSort(A, i, group_end_index)
            median_index = (group_end_index+i)/2
            A[median_index], A[j] = A[j], A[median_index]
            j += 1
        j-=1
        if (j-start+1) <= 5:
            A[start:j+1] = sorted(A[start:j+1])
            #A = InsertionSort(A, start, j)
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

random.seed(100)
#A = [1,2,43,123,41,3,4,5,10,9,8,7,6,13,11,12]
t1 = 0
t2 = 0
list_size = 300
for i in xrange(10):
    A = random.sample(xrange(1000), list_size)
    start_time = time.time()
    print Select(A, 8)
    t1 += time.time() - start_time
    A = random.sample(xrange(long(1000)), list_size)
    start_time = time.time()
    A.sort()
    print A[7]
    t2 += time.time() - start_time


print t1/10
print t2/10
