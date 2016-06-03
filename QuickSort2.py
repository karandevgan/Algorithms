import random;

def Partiton(list, left_index, right_index):
    pivot = list[right_index]
    swap_pointer = left_index
    k = None
    for index in range(left_index, right_index):
        elem = list[index]

        if elem <= pivot:
            list[index], list[swap_pointer] = list[swap_pointer], list[index]
            if (k is None):
                if (elem == pivot):
                    k = swap_pointer
            else:
                list[swap_pointer], list[k] = list[k], list[swap_pointer]
                k += 1

            swap_pointer += 1
    list[swap_pointer], list[right_index] = list[right_index], list[swap_pointer]


#list = [3, 3, 5, 4, 1, 5, 5, 4, 4, 3]
list = [2,10,4,4,1,3,2,6,5,3,3,5]

#list = [random.randint(1,5) for _ in range(10)]
print list
Partiton(list, 0, len(list)-1)
print list
