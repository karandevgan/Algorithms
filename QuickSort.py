import random

def Swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def Partition(list, left_index, right_index):
    pivot = list[right_index]
    partition_index = left_index
    for index in range(left_index, right_index):
        if list[index] <= pivot:
            if partition_index != index:
                Swap(index, partition_index)
            partition_index += 1
    Swap(partition_index, right_index)
    return partition_index

global count
count = 0

def QuickSort(list, left_index, right_index):
    if left_index < right_index:
        partition_index = Partition(list, left_index, right_index)
        QuickSort(list, left_index, partition_index-1)
        QuickSort(list, partition_index+1, right_index)
    global count
    count += 1

random.seed(20)

list = [random.randint(-100,100) for _ in range(20)]
print "Before Sorting:\n", list
QuickSort(list, 0, len(list)-1)
print "After Sorting:\n", list
print "No of times QuickSort is called: ", count;
