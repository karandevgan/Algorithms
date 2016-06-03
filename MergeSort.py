import random

def Merge(list, left_index, dividing_index, right_index):

    left_list = list[left_index:dividing_index+1]
    right_list = list[dividing_index+1:right_index+1]

    left_list.extend([float('inf')])
    right_list.extend([float('inf')])

    left = 0
    right = 0
    for index in range(left_index,right_index+1):
        if left_list[left] <= right_list[right]:
            list[index] = left_list[left]
            left += 1
        else:
            list[index] = right_list[right]
            right += 1
    return list

def MergeSort(list, left_index, right_index):
    if left_index < right_index:
        dividing_index = (left_index + right_index) / 2
        MergeSort(list, left_index, dividing_index)
        MergeSort(list, dividing_index+1, right_index)
        Merge(list, left_index, dividing_index, right_index)

list = [random.randrange(-10,10) for _ in range(20)]

print "Before Sorting:\n", list

MergeSort(list, left_index=0, right_index=len(list)-1)

print "After Sorting:\n", list
