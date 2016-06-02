import random

def Swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def Partition(list, left_index, right_index):
    random_index = random.randint(left_index, right_index)
    partition_index = left_index
    Swap(list, random_index, right_index)
    pivot = list[right_index]
    equal_index = None
    for index in range(left_index, right_index):
        if list[index] < pivot:
            if (equal_index is None):
                if (partition_index != index):
                    Swap(list, index, partition_index)
            else:
                Swap(list, index, equal_index)
                Swap(list, index, partition_index)
                equal_index += 1
            partition_index += 1
        elif list[index] == pivot:
            if (equal_index is None):
                if (partition_index != index):
                    Swap(list, partition_index, index)
                equal_index = partition_index
                partition_index += 1
            else:
                if (partition_index != index):
                    Swap(list, partition_index, index)
                partition_index += 1

    Swap(list, right_index, partition_index)

    if (equal_index is None):
        equal_index = partition_index

    return equal_index, partition_index

global count
count = 0

def QuickSort(list, left_index, right_index):
    if left_index < right_index:
        equal_index, partition_index = Partition(list, left_index, right_index)
        QuickSort(list, left_index, equal_index-1)
        QuickSort(list, partition_index+1, right_index)
    global count
    count += 1

random.seed(20)

list = [random.randint(-100,100) for _ in range(20)]
print "Before Sorting:\n", list
QuickSort(list, 0, len(list)-1)
print "After Sorting:\n", list

print "No of times QuickSort is called: ", count;
