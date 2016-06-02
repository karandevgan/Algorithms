import random

def Parent(index):
    return index / 2


def Left(index):
    return (2 * index) + 2


def Right(index):
    return (2 * index) + 1


def Swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]


def MaxHeapify(list, index, heap_size):
    while True:
        left_index = Left(index)
        right_index = Right(index)
        largest = index
        if (left_index < heap_size) and (list[left_index] > list[index]):
            largest = left_index
        if (right_index < heap_size) and (list[right_index] > list[largest]):
            largest = right_index

        if (largest != index):
            Swap(list, largest, index)
            # MaxHeapify(list, largest)
            index = largest
        else:
            break


def BuildMaxHeap(list):
    mid_list = len(list) / 2
    for index in range(mid_list, -1, -1):
        MaxHeapify(list, index, len(list))

def HeapSort(list):
    sorted_list = []
    BuildMaxHeap(list)
    heap_size = len(list)
    for index in range(len(list)-1, 1, -1):
        Swap(list, 0, index)
        heap_size -= 1
        MaxHeapify(list, 0, heap_size)


random.seed(20)

list = [random.randint(-100,100) for _ in range(20)]
print "Before Sorting:\n", list
HeapSort(list)
print "After Sorting:\n", list
